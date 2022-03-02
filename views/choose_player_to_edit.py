from views.singleton import singleton
from views.choice_view import ChoiceView


@singleton
class ChoosePlayerToEdit(ChoiceView):
    def __init__(self):
        self.title = "Choose the player to edit :"
        self.options = [
            "List of players :  "
        ]
        self.actions = [
            lambda: print("Edit player: "),
        ]
        self.quit_msg = "Returning to main menu"