from views.singleton import singleton
from views.print_view import PrintView

@singleton
class ShowTournamentInfo(PrintView):
    def __init__(self):
        self.title = "Tournament Info"
        self.content_func = None
        self.parent_menu = "Tournament List "
        self.args = "tournament_id"

