from datetime import datetime
# from views import MenuView
from models.player import Player
from serializers.serialized_player import save_players


def players_list():
    return Player.players_list


def validate_date(date_string):
    try:
        date_birth_obj = datetime.strptime(date_string, "%d-%m-%Y")
        return True
    except ValueError as e:
        print(str(e))
        return False


def validate_gender(gender):
    if gender in ["M", "F"]:
        return True
    print("Invalid gender")
    return False


def validate_rank(rank):
    try:
        rank = int(rank)
        if rank <= 0:
            raise TypeError("Rank can't be a negative number nor 0")
        return True
    except TypeError as e:
        print(str(e))
        return False


def validate_id(player_id):
    if player_id in Player.all_ids():
        return True
    else:
        print("Non-existing player id")
        return False


def create_player(first_name, last_name, date_birth, gender, rank):
    player_id = Player.id
    Player(player_id, first_name, last_name, date_birth, gender, int(rank))
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




