@singleton
class ShowAllTournamentsView(ChoiceView):
    print("All tournaments")
    options = [
        "a list of the names of tournaments"
    ]
    actions = [
        pass
    ]

    quit_msg = print("Return to main menu")