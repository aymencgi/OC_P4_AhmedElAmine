from controllers.player_controller import validate_date, create_player, update_player, players_list
from views.input_menu import InputMenu
from operator import itemgetter


class CreatePlayerView(InputMenu):
    def __init__(self):
        self.intro = "Write the info of the player you want to add"
        self.messages = [
            "Player first name: ",
            "Player last name: ",
            "Player date of birth (dd-mm-yyyy): ",
            "Player gender: ",
            "Player rank: "
        ]
        self.function = create_player


class ShowPlayersView:
    @staticmethod
    def start():
        print("List of the players")
        for player in players_list():
            print(player)


class ShowPlayersViewByAlphabet:
    @staticmethod
    def start():
        players_list().sort(key=lambda x: x.first_name.lower())
        for player in players_list():
            print(player)


class ShowPlayersViewByRank:
    @staticmethod
    def start():
        sortd_list = sorted(players_list(), key=lambda x: int(x.rank), reverse=True)
        for player in sortd_list:
            print(player)


class EditPlayerView(InputMenu):
    def __init__(self):
        self.intro = "Choose the id of the player to edit"
        self.messages = [
            "Player id: ",
            "Player's new rank: "
        ]
        self.function = update_player

