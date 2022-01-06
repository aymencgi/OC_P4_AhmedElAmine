from controllers.controller import players_list, create_tournament
from views.player_menu_view import CreatePlayerView, ShowPlayersView, EditPlayerView
from views.tournament_menu_view import CreateTournamentView


class MainMenuView:
    @staticmethod
    def start():
        while True:
            print("Main Menu:")
            print("1- Add a Player")
            print("5- Edit a Player")
            print("2- Lister les joueurs")
            print("3- Create Tournament")
            print("4- Show Players by Alphabetical Order")
            print("0- Quitter")
            choice = input("Votre choix: ")
            if choice == "1":
                CreatePlayerView().start()
            if choice == "2":
                ShowPlayersView.start()
            if choice == "3":
                CreateTournamentView().start()
            if choice == "4":
                ShowPlayersAlphabet()
            if choice == "5":
                ShowPlayersView.start()
                EditPlayerView().start()
            if choice == "0":
                print("Good bye!")
                break

            input("\n\nClick any button to continue")








class ShowPlayersAlphabet:
    @staticmethod
    def sortplayersbyalphabet():
            pass


class ShowPlayersByRank:
    @staticmethod
    def sortplayersbyrank():
            pass





#class CreateTournamentView:
    #@staticmethod
    #def start():
        #print("Create New Tournament")
        #name = input("Tournament Name")
        #place = input("Place of the Tournament")
        #date = input("Date")
        #number_rounds = input("Number of rounds")
        #time_control = input("Time control")
        #description = input("Description")
        #result = create_tournament(name, place, date, number_rounds, time_control, description)
        #print(result)
