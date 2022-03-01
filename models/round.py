class Round:
    round_list = []

    def __init__(self,name,start_date,tournament_id):
        self.name = name
        self.start_date = start_date
        self.end_date = None
        self.match_list = []
        self.tournament_id = tournament_id

    def __repr__(self):
        res = f"id: {self.name} - Round {self.start_date} ({self.tournament_id})\n"
        for match in self.match_list:
            res += str(match) + "\n"

        return res

