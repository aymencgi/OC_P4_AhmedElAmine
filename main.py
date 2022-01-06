from views.MenuView import MainMenuView
from models.serialized_player import save_players, load_players
from models.player import Player


#Player("Ahmed", "Aymen", "01-01-1990", "Male", 100)
#Player("Aamoum", "Anas", "01-01-1988", "Male")
load_players()
MainMenuView.start()


