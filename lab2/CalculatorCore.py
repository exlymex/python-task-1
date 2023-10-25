import math


class CalculatorCore:
    def __init__(self):
        self.memory = None
        self.history = []
        self.settings = {
            "decimal_places": 2,
            "use_memory": True
        }

    def add_to_history(self, expression, value):
        entry = f'{expression} - {value}'
        self.history.append(entry)

    def store_in_memory(self, value):
        self.memory = value

    def retrieve_from_memory(self):
        return self.memory

    def view_history(self):
        if not self.history:
            return 'Empty history'
        return '\n'.join(self.history)

    def calculate_number(self, first_number, second_number, operator):
        try:
            if operator == '-':
                return first_number - second_number
            if operator == '+':
                return first_number + second_number
            if operator == '*':
                return first_number * second_number
            if operator == '%':
                return first_number % second_number
            if operator == '^':
                return first_number ** second_number
            if operator == '√':
                return math.sqrt(first_number)
            if operator == '/':
                if second_number == 0:  # Prevent division by zero
                    raise ValueError("Error: Division by zero.")
                return first_number / second_number
        except Exception as e:
            raise e

    def change_settings(self):
        print("\nSettings Menu:")
        print("1. Change decimal places.")
        print("2. Toggle memory function.")
        print("3. Exit to main menu.")

        choice = input("Enter your choice: ")

        if choice == '1':
            self.change_decimal_places()
        elif choice == '2':
            self.toggle_memory_function()
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

    def change_decimal_places(self):
        try:
            places = int(input("Enter number of decimal places (0-10): "))
            if 0 <= places <= 10:
                self.settings["decimal_places"] = places
                print(f"Set decimal places to {places}.")
            else:
                print("Invalid number of decimal places.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")

    def toggle_memory_function(self):
        self.settings["use_memory"] = not self.settings["use_memory"]
        status = "enabled" if self.settings["use_memory"] else "disabled"
        print(f"Memory function is now {status}.")
