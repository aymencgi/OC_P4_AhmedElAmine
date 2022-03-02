from views.singleton import singleton
from views.print_view import PrintView

@singleton
class ShowAllPlayersOfATournament(PrintView):
    def __init__(self):
        self.title = "Show all players of a tournament "
        self.content_func = None
        self.parent_menu = "Tournament List "

