from controllers.tournament_controller import create_tournament
from views.input_menu import InputMenu



class CreateTournamentView(InputMenu):
    def __init__(self):
        self.messages = [
            "Create New Tournament: ",
            "Tournament Name: ",
            "Place of the Tournament: ",
            "Date: ",
            "Player rank: "
            "Number of rounds: "
            "Time control: "
            "Description: "
        ]
        self.function = create_tournament
