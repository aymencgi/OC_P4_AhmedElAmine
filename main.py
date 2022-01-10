from views.MenuView import MainMenuView
from models.serialized_player import load_players
from models.serialized_tournament import load_tournaments
from models.player import Player


#Player("Ahmed", "Aymen", "01-01-1990", "Male", 100)
#Player("Aamoum", "Anas", "01-01-1988", "Male")
load_tournaments()
load_players()
MainMenuView.start()


