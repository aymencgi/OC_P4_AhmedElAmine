from views.singleton import singleton
from views.choice_view import ChoiceView
from views.player_show_method_view import ShowPlayersMethod
from views.show_all_tournaments_view import ShowAllTournamentsView
from views.choose_player_to_edit import ChoosePlayerToEdit
from views.show_all_tournaments_view import ShowAllTournamentsView


@singleton
class MainMenuView(ChoiceView):
    def __init__(self):
        self.title = "*** Main Menu ***\n###############"

        self.options = [
            "Add player",
            "Edit player",
            "Create tournament",
            "Play tournament",
            "Show all players",
            "Show all players of a tournament",
            "List of all the tournaments"

        ]
        self.actions = [
            lambda: print("1"),
            ChoosePlayerToEdit().start,
            lambda: print("3"),
            lambda: print("4"),
            ShowPlayersMethod().start,
            lambda: print("6"),
            ShowAllTournamentsView().start,
        ]
        self.quit_msg = "Good bye!"

