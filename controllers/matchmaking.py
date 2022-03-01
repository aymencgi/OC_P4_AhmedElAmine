from models.player import Player


def generate_first_round_matches(players_ids):
    try:
        players = [Player.find_player(x) for x in players_ids]
    except ValueError as e:
        return str(e)
    players_sorted = sorted(players, key=lambda x: x.rank, reverse=True)

    l = len(players)
    pl_1 = players_sorted[: l // 2]
    pl_2 = players_sorted[l // 2:]

    return zip(pl_1, pl_2)


def adding_points():
    adding_p1 = player_1
    adding_p2 = player_2
    results = []
    points = 0
    if results == "1":
        adding_p2 = points + 1
    elif results == "2":
        adding_p2 = points + 1
    elif results == "3":
        adding_p1 = points + 0.5
        adding_p2 = points + 0.5


