from models.tournament import Tournament
from models.player import Player
from models.serialized_tournament import save_tournament
from player_controller import players_list
from datetime import datetime


def tournament_list():
    return Tournament.tournament_list


def active_tournament_list():
    return [tournament for tournament in Tournament.tournament_list if tournament.end_date is None]


def validate_start_date(start_date):
    try:
        date_birth_obj = datetime.strptime(start_date, "%d-%m-%Y")
        return True
    except ValueError as e:
        print(str(e))
        return False


def validate_number_rounds(number_rounds):
    try:
        number_rounds = int(number_rounds)
        return True
    except ValueError as e:
        return False


def validate_time_control(time_control):
    if time_control in ["1", "2", "3"]:
        return True
    return False


def validate_number_player(number_players):
    try:
        number_players = int(number_players)
        return True
    except ValueError as e:
        return False


def create_tournament(name, place, start_date, number_rounds, time_control, description, number_players):
    tc = {
        "1": "Blitz",
        "2": "Bullet",
        "3": "Rapid"
    }
    tournament_id = Tournament.id
    Tournament(tournament_id, name, place, start_date, None, int(number_rounds), [],
               tc[time_control], description, int(number_players), [])
    save_tournament()
    return f"Creating Tournament {name} Added"


def add_players(ids):
    ids_list = ids.split()
    ids_set = set(ids_list)
    players = players_list()
    tournament = Tournament.tournament_list[-1]

    for player in players:
        if str(player.player_id) in ids_set:
            tournament.players.append(player.player_id)
            print(f"Player {player} added to the tournament")
    save_tournament()


def validate_added_players(ids):
    tournament = Tournament.tournament_list[-1]
    num_players = tournament.number_players

    ids_set = set(ids.split())
    if len(ids_set) != num_players:
        print("Incorrect number of players")
        return False

    for elm in ids_set:
        if int(elm) not in Player.all_ids():
            print(f"Player Id {elm} doesn't exist")
            return False

    return True


def validate_id(tournament_id):
    if int(tournament_id) in Tournament.all_active_ids():
        return True
    else:
        print("Non-existing tournament id")
        return False
