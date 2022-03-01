
class Player:
    players_list = []
    id = 1

    def __init__(self, player_id, first_name, last_name, date_of_birth, gender, rank):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank
        Player.players_list.append(self)
        Player.id += 1

    def __repr__(self):
        return f"id: {self.player_id} - Player {self.first_name} {self.last_name} ({self.gender}), ranked: {self.rank}"

    @staticmethod
    def all_ids():
        return [item.player_id for item in Player.players_list]

    @staticmethod
    def find_player(player_id):
        for player in Player.players_list:
            if player.player_id == player_id:
                return player

        raise ValueError("Not existing player id")