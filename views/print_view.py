class PrintView:
    def __init__(self):
        self.title = ""
        self.content_func = None
        self.parent_menu = ""
        self.args = []

    def start(self):
        to_print = self.content_func(self.args)
        print("#########")
        print(self.title)
        print("-----------")
        print(to_print)
        input(f"Click any button to return to {self.parent_menu}")


