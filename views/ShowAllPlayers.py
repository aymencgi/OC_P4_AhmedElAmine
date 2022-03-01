@singleton
class ShowAllPlayers(ChoiceView):
    print("Show all players Menu")
    options = [
        "Show plyaers by rank",
        "Show players by alphabetical order"
    ]
    actions = [
        pass
    ]

    quit_msg = print("Return to main menu")