class Tournament:
    tournament_list = []
    id = 1

    def __init__(self, tournament_id, name, place, start_date, end_date, number_rounds, rounds, time_control, description, number_players, players):
        self.tournament_id = tournament_id
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.number_rounds = number_rounds
        self.rounds = rounds
        self.time_control = time_control
        self.description = description
        self.number_players = number_players
        self.players = players
        Tournament.tournament_list.append(self)
        Tournament.id += 1

    def __str__(self):
        return f"{self.name}, {self.place}"