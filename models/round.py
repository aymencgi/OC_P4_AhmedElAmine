class Round:
    round_list = []

    def __init__(self,name,date_start,date_end,match_list,tournament_id):
        self.name = name
        self.date_start = date_start
        self.date_end = date_end
        self.match_list = match_list
        self.tournament_id = tournament_id
        Round.round_list.append(self)

