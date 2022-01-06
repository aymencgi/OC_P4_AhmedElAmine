from views import MenuView
from models.player import Player
from models.tournament import Tournament
from models.round import Round


def players_list():
    return Player.players_list


def create_player(first_name, last_name, date_birth, gender, rank):
    try:
        rank = int(rank)
    except TypeError as e:
        return "The rank is not an integer"

    Player(first_name, last_name, date_birth, gender, rank)
    return f"Player {first_name} {last_name} added"


def create_tournament(name, place, date, number_rounds, time_control, description):
    Tournament(name, place, date, number_rounds, time_control, description)
    return f"Creating Tournament {name} Added"


def create_rounds(name,date_start,date_end,match_list,tournament_id):
    Round(name,date_start,date_end,match_list,tournament_id)
    return f"Creating Rounds {name}, {date_start} Added"


