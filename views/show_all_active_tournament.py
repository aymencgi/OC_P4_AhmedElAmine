from views.singleton import singleton
from views.choice_view import ChoiceView


@singleton
class ShowAllactiveTournament(ChoiceView):
    def __init__(self):
        self.title = "List of active tournaments  :"
        self.options = [
            "A list of all the active tournaments "
        ]
        self.actions = [
            lambda: print("List of all the active tournaments : "),
        ]
        self.quit_msg = "Returning to main menu"