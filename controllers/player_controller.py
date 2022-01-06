from datetime import datetime
from views import MenuView
from models.player import Player
from models.serialized_player import save_players


def players_list():
    return Player.players_list


def validate_date(date_string):
    try:
        date_birth_obj = datetime.strptime(date_string, "%d-%M-%Y")
        return 1
    except ValueError as e:
        print(str(e))
        return "Wrong date format"


def create_player(first_name, last_name, date_birth, gender, rank):
    try:
        rank = int(rank)
    except TypeError as e:
        return "The rank is not an integer"

    player_id = Player.id
    Player(player_id, first_name, last_name, date_birth, gender, rank)
    save_players()
    return f"Player {first_name} {last_name} added"


def update_player(id, rank):
    players = players_list()

    for player in players:
        if player.player_id == int(id):
            try:
                player.rank = int(rank)
                save_players()
                return f"Player with ID :{id} has been updated"
            except:
                return "Error: rank is not an integer"

    return f"id not found"




