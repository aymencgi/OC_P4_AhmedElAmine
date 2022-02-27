from tinydb import TinyDB,Query
from models.player import Player


def save_players():
    serialized_players = []
    for player in Player.players_list:
        serialized_player = {
            "player_id": player.player_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "date_of_birth": player.date_of_birth,  # strftime
            "gender": player.gender,
            "rank": player.rank,

        }

        serialized_players.append(serialized_player)

    db = TinyDB('db.json', indent=4, separators=(',', ': '))
    players_table = db.table("players")
    players_table.truncate()
    players_table.insert_multiple(serialized_players)


def load_players():
    db = TinyDB("db.json")
    players_table = db.table("players")
    serialized_players = players_table.all()
    for player in serialized_players:
        # Player(player["first_name"], player["last_name"], player["date_of_birth"],
        #        player["gender"], player["rank"])
        Player(**player)






