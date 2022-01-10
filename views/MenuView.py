from views.player_menu_view import CreatePlayerView, ShowPlayersView, EditPlayerView,ShowPlayersViewByAlphabet,ShowPlayersViewByRank
from views.tournament_menu_view import CreateTournamentView,ShowTournamentView


class MainMenuView:
    @staticmethod
    def start():
        while True:
            print("Main Menu:")
            print("1- Add a Player")
            print("2- Start new tournament")
            print("3- Show all players")
            print("4- List all the Tournaments")
            print("5- Edit a Player")
            print("0- Quitter")
            choice = input("Votre choix: ")
            if choice == "1":
                CreatePlayerView().start()
            if choice == "2":
                CreateTournamentView().start()
            if choice == "3":
                print("-----------a Show all players by alphabetical order")
                print("-----------b Show all players by rank")
                second_choice = input("Choose a or b: ")
                if second_choice == "a":
                    ShowPlayersViewByAlphabet.start()
                if second_choice == "b":
                    ShowPlayersViewByRank.start()
            if choice == "4":
                ShowTournamentView().start()
            if choice == "5":
                ShowPlayersView.start()
                EditPlayerView().start()
            if choice == "0":
                print("Good bye!")
                break

            input("\n\nClick any button to continue")
