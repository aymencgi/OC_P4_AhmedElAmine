class Round:
    round_list = []

    def __init__(self,name,start_date,tournament_id):
        self.name = name
        self.start_date = start_date
        self.date_end = None
        self.match_list = []
        self.tournament_id = tournament_id
        Round.round_list.append(self)

