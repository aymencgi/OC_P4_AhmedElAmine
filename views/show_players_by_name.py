from views.singleton import singleton
from views.print_view import PrintView

@singleton
class ShowPlayersByName(PrintView):
    def __init__(self):
        self.title = "All players sorted by name"
        self.content_func = None
        self.parent_menu = "Show all players Menu"
        self.args = None