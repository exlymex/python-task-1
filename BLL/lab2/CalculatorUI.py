from BLL.lab2.CalculatorCore import CalculatorCore


class CalculatorUI(CalculatorCore):

    OPERATOR_LIST = ['+', '-', '*', '/', '%', '^', '√']

    def get_user_choice(self):
        return input("Enter your choice: ")

    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Incorrect number! Enter a valid number.")

    def get_operator(self):
        while True:
            operator = input('Enter your operator: ')
            if operator in self.OPERATOR_LIST:
                return operator
            else:
                print('Incorrect operator.')

    def perform_calculation(self):
        first_number = self.get_first_number()
        second_number = self.get_float_input('Enter second number: ')
        operator = self.get_operator()

        result = self.calculate_number(first_number, second_number, operator)
        self.display_and_store_result(first_number, second_number, operator, result)

    def get_first_number(self):
        if self.memory and input('Get value from memory? Y/N: ').strip().upper() == 'Y':
            return self.memory
        return self.get_float_input('Enter first number: ')

    def display_and_store_result(self, first_number, second_number, operator, result):
        expression = f"{first_number} {operator} {second_number}"
        self.add_to_history(expression, result)
        if self.settings["decimal_places"] != 0:
            result = round(result, self.settings["decimal_places"])
        print(result)
        if self.settings["use_memory"]:
            self.store_in_memory(result)

    def run_calculator(self):
        while True:
            print("\nCalculator Menu:")
            print("1. Perform calculation.")
            print("2. View history.")
            print("3. Change settings.")
            print("4. Quit.")

            user_choice = self.get_user_choice()

            if user_choice == '1':
                self.perform_calculation()
            elif user_choice == '2':
                print(self.view_history())
            elif user_choice == '3':
                self.change_settings()
            elif user_choice == '4':
                break
