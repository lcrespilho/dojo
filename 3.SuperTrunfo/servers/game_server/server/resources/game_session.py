from time import time
import random
from error_codes import error_codes
import sys
from thread import start_new_thread

from player import Player
from base_socket import BaseSocket
import game_logic


class GameSession(BaseSocket):
    id = None
    begin = None
    last_interaction = None
    interaction_timeout = 60
    session_timeout = 300
    active = True
    game_state = None
    player_1 = Player()
    player_2 = Player()

    def __init__(self, addr=None):
        self.address = addr
        self.generate_id()
        self.begin = time()
        self.last_interaction = time()
        self.game_state = game_logic.GameLogic()
        start_new_thread(self.session_loop, ())

    def generate_id(self):
        beginning_of_day_in_millis = int(time() / 86400) * 86400000
        epoch_in_millis = int(time() * 1000)
        day_millis = epoch_in_millis - beginning_of_day_in_millis
        self.id = str(format(day_millis, '08')) + str(format(random.getrandbits(16), '05'))

    def serialize(self):
        return {
            'begin': self.begin,
            'id': self.id,
            'last_interaction': self.last_interaction,
            'player_1': str(self.player_1.id),
            'player_2': str(self.player_2.id),
        }

    def inactivate_sessions(self, error):
        if not error or error not in error_codes:
            data = {'code': 0, 'message': 'Unknown error'}
        else:
            data = error_codes[error]

        self._send_dict(data, self.player_1.connection)
        self._send_dict(data, self.player_2.connection)
        self.active = False

    def check_timeout(self):
        if time() - self.last_interaction > self.interaction_timeout:
            self.inactivate_sessions('inactive_timeout')

        if time() - self.begin > self.session_timeout:
            self.inactivate_sessions('timeout')

    def can_player_join(self, player_id):
        can_join_on_1 = (self.player_1.id is None and self.player_2.id != player_id)
        can_join_on_2 = (self.player_2.id is None and self.player_1.id != player_id)
        return can_join_on_1 or can_join_on_2

    def communicate_game_logic(self, player_1_data, player_2_data):
        response = dict()

        if player_1_data:
            response[self.player_1.id] = self.game_state.process_input(player_1_data, 1)
        elif player_1_data is False:
            self.inactivate_sessions('invalid_message')

        if player_2_data:
            response[self.player_2.id] = self.game_state.process_input(player_2_data, 2)
        elif player_2_data is False:
            self.inactivate_sessions('invalid_message')
        if response:
            self._send_dict(self.player_1.connection, response)
            self._send_dict(self.player_2.connection, response)

    def add_player(self, player_id, connection):
        new_player = Player(connection=connection, id=player_id)

        if self.player_1.id is None:
            self.player_1 = new_player
        else:
            self.player_2 = new_player

    def close(self):
        if self.player_1.connection:
            self.player_1.connection.close()

        if self.player_2.connection:
            self.player_2.connection.close()

    def session_loop(self):
        while self.active:
            player_1_data = self._receive_dict_async(self.player_1.connection)
            player_2_data = self._receive_dict_async(self.player_2.connection)
            self.communicate_game_logic(player_1_data, player_2_data)
        self.game_state.end_match()
        sys.exit(0)
