from views.singleton import singleton
from views.input_view import InputView


@singleton
class CreatePlayer(InputView):
    def __init__(self):
        self.intro = "Add tournament details"
        self.message = [
            "Tournament name :",
            "Tournament place :",
            "Description :",
            "number of players :",
            "players ids :",
            "number of rounds :",
            "create_tournament(to be found in the controllers)",
        ]
        self.function = "edit_player(player_id, rank)"
        self.validators = []
