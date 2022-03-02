class ChoiceView:
    def __init__(self):
        self.title = ""
        self.options = []
        self.actions = []
        self.quit_msg = ""

    def start(self):
        while True:
            print("###########################")
            print(self.title)
            for i, opt in enumerate(self.options, start=1):
                print(f"{i} - {self.options[i - 1]}")
            print("0 - Cancel")
            choice = input("What's your choice: ")
            try:
                if int(choice) > 0:
                    print("Choice is positive int")
                    self.actions[int(choice) - 1]()
                elif int(choice) == 0:
                    print(f"{self.quit_msg}")
                    break
                else:
                    raise Exception("Wrong Choice")
            except:
                print("Invalid Choice. Try again")

            input("Press any key to continue...")
