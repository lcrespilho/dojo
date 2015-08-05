class BaseState(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def transition(self, input_data, player=None):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError


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
                "action": "user_joined",
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
            message[0] = message[1] = {"action": "user_ready",
                       "player_id": input_data["player_id"],
                       "game_start": False}
            self.players_ready.append(input_data["player_id"])
            if len(self.players_ready) == 2:
                message[0]["game_start"] = message[1]["game_start"] = True
                return TurnState(self.game_data), message
        return self, message


class TurnState(BaseState):
    pass
    # def transition(self, input_data):
    #     if "selected_attribute" in input_data:
    #         tmp_attribute = input_data["selected_attribute"]
    #     deck1 = self.game_data["deck1"]
    #     deck2 = self.game_data["deck2"]


class EndState(BaseState):
    pass


class GameLogic(object):
    def __init__(self):
        self.game_data = {
            "players": [],
        }

        self.game_state = InitialState(self.game_data)

    def process_input(self, data, player):
        transition_return = self.game_state.transition(data, player)
        self.game_state = transition_return[0]

        return transition_return[1]

    def end_match(self):
        print 'Bye game!'
