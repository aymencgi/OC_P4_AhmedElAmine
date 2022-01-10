from controllers.tournament_controller import create_tournament,tournament_list
from views.input_menu import InputMenu


class CreateTournamentView(InputMenu):
    def __init__(self):
        self.intro = ""
        self.messages = [
            "Tournament Name: ",
            "Place of the Tournament: ",
            "Start Date: ",
            "Number of rounds: ",
            "Time control: ",
            "Description: ",
        ]
        self.function = create_tournament


class ShowTournamentView:
    @staticmethod
    def start():
        print("List of all the tournaments")
        for tournament in tournament_list():
            print(tournament)