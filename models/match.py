from models.player import Player
from controllers.player_controller import players_list


class Match:
    def __init__(self, p1_id, p2_id):
        self.p1_id = p1_id
        self.p2_id = p2_id
        self.result = None

    def __repr__(self):

        def player_name_1():
            players = players_list()

            for player in players:
                if self.p1_id == player.player_id:
                    return f"{player.first_name}"

        def player_name_2():
            players = players_list()

            for player in players:
                if self.p2_id == player.player_id:
                    return f"{player.first_name}"

        return f'{player_name_1()} VS {player_name_2()} Result : {self.result}'
