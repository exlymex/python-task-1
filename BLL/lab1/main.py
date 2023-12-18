import math

memory = None

history = []

settings = {
    "decimal_places": 2,
    "use_memory": True
}


def add_to_history(expression, value):
    entry = f'{expression} - {value}'
    history.append(entry)


def store_in_memory(value):
    global memory
    memory = value


def retrieve_from_memory():
    global memory
    return memory


def view_history():
    if not history:
        print('Empty history')
        return
    for entry in history:
        print(entry)


def change_settings():
    global settings
    print("1. Change decimal places.")
    print("2. Toggle memory function.")

    choice = input("Enter your choice: ")
    if choice == '1':
        try:
            places = int(input("Enter number of decimal places (0-10): "))
            if 0 <= places <= 10:
                settings["decimal_places"] = places
                print(f"Set decimal places to {places}.")
            else:
                print("Invalid number of decimal places.")
        except ValueError:
            print("Invalid input.")
    elif choice == '2':
        settings["use_memory"] = not settings["use_memory"]
        status = "enabled" if settings["use_memory"] else "disabled"
        print(f"Memory function is now {status}.")


def calculate_number(first_number, second_number, operator):
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
                print("Error: Division by zero.")
                return None
            return first_number / second_number
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def get_correct_operator():
    operator_list = ['+', '-', '*', '/', '%', '^', '√)']
    while True:
        operator = input('Enter your operator\n')
        if operator in operator_list:
            return operator
        else:
            print('Incorrect operator')


def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Incorrent number! Enter valid")


def run_calculator():
    global memory

    while True:
        print("\nCalculator Menu:")
        print("1. Perform calculation.")
        print("2. View history.")
        print("3. Change settings.")
        print("4. Quit.")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            if memory is not None:
                print(f'Number in memory {memory}')
                get_from_memory = input('Get value from memory? Y/N \n').upper()
                if get_from_memory == 'Y':
                    first_number = memory
                else:
                    first_number = get_float_input('Enter first number\n')
            else:
                first_number = get_float_input('Enter first number\n')

            second_number = get_float_input('Enter second number\n')
            operator = get_correct_operator()

            result = calculate_number(first_number, second_number, operator)

            expression = f"{first_number} {operator} {second_number}"
            add_to_history(expression, result)
            if settings["decimal_places"] == 0:
                result = int(round(result))
            else:
                result = round(result, settings["decimal_places"])
            print(result)

            if settings["use_memory"]:
                store_in_memory(result)


        elif user_choice == '2':
            view_history()
        elif user_choice == '3':
            change_settings()
        elif user_choice == '4':
            break


if __name__ == '__main__':
    run_calculator()
