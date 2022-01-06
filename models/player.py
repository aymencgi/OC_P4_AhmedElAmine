
class Player:
    players_list = []
    id = 1

    def __init__(self, player_id, first_name, last_name, date_of_birth, gender, rank=0):
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank
        Player.players_list.append(self)
        Player.id += 1

    def __str__(self):
        return f"id: {self.player_id} - Player {self.first_name} {self.last_name} ({self.gender}), ranked: {self.rank}"

