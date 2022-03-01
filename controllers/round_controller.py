from datetime import date, datetime
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.serialized_tournament import save_tournament
from controllers.matchmaking import generate_first_round_matches

from pprint import pprint


def generate_first_round(tournament_id):
    try:
        tournament = Tournament.find_tournament(tournament_id)
    except ValueError as e:
        return str(e)

    if len(tournament.rounds) != 0:
        return "First round already existing"

    matches = generate_first_round_matches(tournament.players)

    first_round = Round("1", datetime.strftime(datetime.today(), "%d-%m-%Y"), tournament_id)

    for match in matches:

        first_round.match_list.append(
            Match(match[0].player_id, match[1].player_id)
        )

    tournament.rounds.append(first_round)
    pprint(tournament)
    save_tournament()


