class Tournament:
    tournament_list = []

    def __init__(self, name, place, date, number_rounds, time_control, description):
        self.id = len(Tournament.tournament_list) + 1
        self.name = name
        self.place = place
        self.date = date
        self.number_rounds = number_rounds
        self.list_rounds = []
        self.list_players = []
        self.time_control = time_control
        self.description = description
        Tournament.tournament_list.append(self)

    def __str__(self):
        return f"{self.name}, {self.place}"