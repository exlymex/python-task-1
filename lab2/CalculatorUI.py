from lab2.CalculatorCore import CalculatorCore

class CalculatorUI(CalculatorCore):
    def get_float_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except:
                print("Incorrent number! Enter valid")

    def get_correct_operator(self):
        operator_list = ['+', '-', '*', '/', '%', '^', '√']
        while True:
            operator = input('Enter your operator\n')
            if operator in operator_list:
                return operator
            else:
                print('Incorrect operator')

    def run_calculator(self):
        while True:
            print("\nCalculator Menu:")
            print("1. Perform calculation.")
            print("2. View history.")
            print("3. Change settings.")
            print("4. Quit.")
            user_choice = input("Enter your choice: ")

            if user_choice == '1':
                if self.memory is not None:
                    print(f'Number in memory {self.memory}')
                    get_from_memory = input('Get value from memory? Y/N \n').upper()
                    if get_from_memory == 'Y':
                        first_number = self.memory
                    else:
                        first_number = self.get_float_input('Enter first number\n')
                else:
                    first_number = self.get_float_input('Enter first number\n')

                second_number = self.get_float_input('Enter second number\n')
                operator = self.get_correct_operator()

                result = self.calculate_number(first_number, second_number, operator)

                expression = f"{first_number} {operator} {second_number}"
                self.add_to_history(expression, result)
                if self.settings["decimal_places"] == 0:
                    result = int(round(result))
                else:
                    result = round(result, self.settings["decimal_places"])
                print(result)

                if self.settings["use_memory"]:
                    self.store_in_memory(result)

            elif user_choice == '2':
                print(self.view_history())
            elif user_choice == '3':
                self.change_settings()
            elif user_choice == '4':
                break
