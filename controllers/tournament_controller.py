from models.tournament import Tournament


def create_tournament(name, place, date, number_rounds, time_control, description):
    Tournament(name, place, date, number_rounds, time_control, description)
    return f"Creating Tournament {name} Added"