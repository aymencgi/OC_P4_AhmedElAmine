from models.tournament import Tournament
from models.serialized_tournament import save_tournament


def tournament_list():
    return Tournament.tournament_list


def create_tournament(name, place, start_date, number_rounds, time_control, description):
    tournament_id = Tournament.id
    Tournament(tournament_id, name, place, start_date, None, number_rounds, [], time_control, description)
    save_tournament()
    return f"Creating Tournament {name} Added"
