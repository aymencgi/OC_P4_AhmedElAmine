from views.singleton import singleton
from views.choice_view import ChoiceView


@singleton
class ShowAllTournamentsView(ChoiceView):
    def __init__(self):
        self.title = "All tournaments :"
        self.options = [
            "List of tournaments "
        ]
        self.actions = [
            lambda: print("List of tournaments: "),
        ]
        self.quit_msg = "Returning to main menu"