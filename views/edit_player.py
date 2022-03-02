from views.singleton import singleton
from views.input_view import InputView


@singleton
class EditPlayers(InputView):
    def __init__(self):
        self.intro = "Edit Player Rank\nPlayer: son_nom\nCurrent Rank: son_rank"
        self.message = [
            "New Rank :",
        ]
        self.function = "edit_player(player_id, rank)"
        self.validators = []
