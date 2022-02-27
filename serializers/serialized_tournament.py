from tinydb import TinyDB,Query
from models.tournament import Tournament
from models.round import Round
from serialized_round import serialize_rounds, load_round


def save_tournament():
    serialized_tournaments = []
    for tournament in Tournament.tournament_list:
        serialized_tournament = {
            'tournament_id': tournament.tournament_id,
            "name": tournament.name,
            "place": tournament.place,
            "start_date": tournament.start_date,
            "end_date": tournament.end_date,
            "number_rounds": tournament.number_rounds,
            "rounds": serialize_rounds(tournament.rounds),
            "time_control": tournament.time_control,
            "description": tournament.description,
            "number_players": tournament.number_players,
            "players": tournament.players,
        }

        serialized_tournaments.append(serialized_tournament)



    db = TinyDB("db.json", indent=4, separators=(',', ': '))
    tournament_table = db.table("tournaments")
    tournament_table.truncate()
    tournament_table.insert_multiple(serialized_tournaments)


def load_tournaments():
    db = TinyDB("db.json")
    tournament_table = db.table("tournaments")
    serialized_tournaments = tournament_table.all()
    for tournament in serialized_tournaments:
        t = Tournament(**tournament)

        rounds = []
        for r in t.rounds:
            rounds.append(load_round(r))

        t.rounds = rounds


