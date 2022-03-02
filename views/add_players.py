from views.singleton import singleton
from views.input_view import InputView


@singleton
class AddPlayers(InputView):
    def __init__(self):
        self.intro = "Add player details"
        self.message = [
            "Player first name:",
            "Player last name:",
            "Date of Birth:",
            "Gender:",
            "Rank:",
        ]
        self.function = ""
        self.validators = []
