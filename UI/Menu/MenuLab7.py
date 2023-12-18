
from colorama import Fore, Style


class MenuLab7:
    def __init__(self, api_app, validator, reader_writer):
        self.api_app = api_app
        self.validator = validator
        self.reader_writer = reader_writer
        self.menu_options = ["Check weather", "Check wind information", "Check if it will snow", "View History", "Exit"]

    def display_options(self):
        print("Weather Checker Menu")
        for i, option in enumerate(self.menu_options):
            print(f"{i + 1}. {option}")

    def run(self):
        while True:
            self.display_options()
            choice = self.validator.validate_input("Choose an option (1/2/3/4/5/6): ", ['1', '2', '3', '4', '5', '6'])

            if choice == '1':
                city = self.reader_writer.read_input("Enter the city name: ")

                self.api_app.run(choice,city)

            elif choice == '2':
                city = self.reader_writer.read_input("Enter the city name: ")

                self.api_app.run(choice,city)

            elif choice == '3':
                city = self.reader_writer.read_input("Enter the city name: ")
                self.api_app.run(choice, city)

            elif choice == '4':
                self.api_app.history.view_history()

            elif choice == '5':
                print("Goodbye!")
                break
