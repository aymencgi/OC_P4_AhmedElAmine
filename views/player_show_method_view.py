from views.singleton import singleton
from views.choice_view import ChoiceView
from views.show_players_by_rank import ShowPlayersByRank

@singleton
class ShowPlayersMethod(ChoiceView):
    def __init__(self):
        self.title = "*** How would you like to list the players ***\n###############"
        self.options = [
            "Show players by rank",
            "Show players by Alphabetical order",
        ]
        self.actions = [
            lambda: print("Showing by rank"),
            lambda: print("Showing by Alphabetical order")
        ]
        self.quit_msg = "Returning to main menu"
