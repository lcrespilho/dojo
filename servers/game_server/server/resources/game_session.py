from time import time
import random
from error_codes import error_codes
import sys
from thread import start_new_thread

from player import Player
from base_socket import BaseSocket
import game_logic


class GameSession(BaseSocket):
    interaction_timeout = 6000
    session_timeout = 30000

    def __init__(self, addr=None):
        self.id = None
        self.address = addr
        self.generate_id()
        self.begin = time()
        self.last_interaction = time()
        self.game_state = game_logic.GameLogic()
        self.active = True
        self.players = [Player(), Player()]


    def generate_id(self):
        beginning_of_day_in_millis = int(time() / 86400) * 86400000
        epoch_in_millis = int(time() * 1000)
        day_millis = epoch_in_millis - beginning_of_day_in_millis
        self.id = str(format(day_millis, '08')) + str(format(random.getrandbits(16), '05'))

    def serialize(self):
        data = {
            'begin': self.begin,
            'id': self.id,
            'last_interaction': self.last_interaction,
        }

        for idx, player in enumerate(self.players):
            data['player_%d' % idx] = str(player.id),

        return data

    def inactivate_sessions(self, error):
        if not error or error not in error_codes:
            data = {'code': 0, 'message': 'Unknown error'}
        else:
            data = error_codes[error]

        for player in self.players:
            self._send_dict(data, player.connection)
        self.active = False

    def check_timeout(self):
        if time() - self.last_interaction > self.interaction_timeout:
            self.inactivate_sessions('inactive_timeout')

        if time() - self.begin > self.session_timeout:
            self.inactivate_sessions('timeout')

    def can_player_join(self, player_id):
        for player in self.players:
            if player.id is None:
                return True
        return False

    def add_player(self, player_id, connection):
        new_player = Player(connection=connection, id=player_id)
        message = [None]*len(self.players)

        for idx, player in enumerate(self.players):
            if player.id is None:
                self.players[idx] = new_player
                message[idx] = {"action": "player_joined", "player_id": player_id}
                self.communicate_game_logic(message)
                break

    def communicate_game_logic(self, player_data):
        for player_idx, player in enumerate(self.players):
            if player_data[player_idx]:
                response = self.game_state.process_input(player_data[player_idx], player_idx)
                self.broadcast_game_logic_response(response)

            elif player_data[player_idx] is False:
                self.inactivate_sessions('invalid_message')

    def broadcast_game_logic_response(self, response):
        for response_idx, response_for_player in enumerate(response):
            if response_for_player:
                self._send_dict(self.players[response_idx].connection, response_for_player)


    def close(self):
        for player in self.players:
            if player.connection:
                player.connection.close()

    def session_loop(self):

        while self.active:
            player_data = [None]*len(self.players)

            for player_idx, player in enumerate(self.players):
                player_data[player_idx] = self._receive_dict_async(player.connection)

            self.communicate_game_logic(player_data)

        self.game_state.end_match()
        sys.exit(0)
