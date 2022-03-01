from models.match import Match


def serialize_matches(matches):
    serialized_matches = []
    for m in matches:
        serialized_matches.append({
            "p1_id": m.p1_id,
            "p2_id": m.p2_id,
            "result": m.result,
        })

    return serialized_matches


def load_match(match):
    match_obj = Match(match["p1_id"], match["p2_id"])
    match_obj.result = match["result"]
    return match_obj
