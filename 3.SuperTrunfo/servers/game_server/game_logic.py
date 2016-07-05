from random import shuffle, randrange


class BaseState(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def transition(self, input_data, player=None):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError

    def _pop_player_card(self, player):
        return self.game_data['player_decks'][player].pop()


class InitialState(BaseState):
    def __init__(self, game_data):
        super(InitialState, self).__init__(game_data)
        self.count = 0

    def transition(self, input_data, player=None):
        message = [None, None]

        if input_data["action"] == "player_joined":
            self.count += 1
            self.game_data["players"].append(input_data["player_id"])

            message[(player + 1) % 2] = {
                "action": "player_joined",
                "player_id": input_data["player_id"],
                "room_ready": False
            }

            message[player] = {
                "action": "room_joined",
                "other_players": self.game_data['players'][:-1],
                "room_ready": False
            }

            if self.count == 2:
                message[0]["room_ready"] = message[1]["room_ready"] = True
                return WaitingState(self.game_data), message
        return self, message


class WaitingState(BaseState):
    def __init__(self, game_data):
        super(WaitingState, self).__init__(game_data)
        self.players_ready = []

    def transition(self, input_data, player=None):
        message = [None, None]

        if input_data["action"] == "player_ready":
            message[0] = message[1] = {"action": "player_ready",
                                       "player_id": input_data["player_id"],
                                       "game_start": False}
            self.players_ready.append(input_data["player_id"])
            if len(self.players_ready) == 2:
                message[0]["game_start"] = message[1]["game_start"] = True
                message[0]["card"] = self._pop_player_card(0)
                message[1]["card"] = self._pop_player_card(1)
                return TurnState(self.game_data), message
        return self, message


class TurnState(BaseState):
    def transition(self, input_data, player=None):
        if player != self.game_data["current_player"]:
            return self, [None, None]


class EndState(BaseState):
    pass


class GameLogic(object):
    def __init__(self, deck_cards, attributes):
        shuffle(deck_cards)

        self.game_data = {
            "players": [],
            "player_decks": [[], []],
            "deck_cards": deck_cards,
            "attributes": attributes,
            "current_player": randrange(0, 2)
        }

        self._separate_decks()
        self.game_state = InitialState(self.game_data)

    def _separate_decks(self):
        half_deck_size = int(len(self.game_data['deck_cards']) / 2)
        self.game_data['player_decks'][0] = self.game_data['deck_cards'][half_deck_size:]
        self.game_data['player_decks'][1] = self.game_data['deck_cards'][:-half_deck_size]

    def process_input(self, data, player):
        transition_return = self.game_state.transition(data, player)
        self.game_state = transition_return[0]

        return transition_return[1]

    def end_match(self):
        print 'Bye game!'
