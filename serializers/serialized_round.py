from serializers.serialized_match import serialize_matches, load_match
from models.round import Round


def serialize_rounds(rounds):
    serialized_rounds = []
    for r in rounds:
        serialized_rounds.append({
            "name": r.name,
            "start_date": r.start_date,
            "end_date": r.end_date,
            "match_list": serialize_matches(r.match_list),
            "tournament_id": r.tournament_id,
        })

    return serialized_rounds


def load_round(round_dict):
    matches = []
    for match in round_dict["match_list"]:
        matches.append(load_match(match))

    round_obj = Round(round_dict["name"], round_dict["start_date"], round_dict["tournament_id"])
    round_obj.end_date = round_dict["end_date"]
    round_obj.match_list = matches

    return round_obj
