class InputMenu:
    def __init__(self):
        self.intro = ""
        self.messages = []
        self.function = None
        self.validators = []

    def start(self):
        args = []
        print(self.intro)
        for message in self.messages:
            print("0 - Cancel adding")
            choice = input(message)

            if choice == "0":
                return "Adding Cancelled"
            else:
                args.append(choice)
        result = self.function(*args)
        print(result)
