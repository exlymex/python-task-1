import re


class Validator:
    def __init__(self, input_parser):
        self.input_parser = input_parser

    def validate_input(self, prompt, valid_options):
        while True:
            user_input = input(prompt)
            if user_input not in valid_options:
                print("Invalid input. Please try again.")
            else:
                return user_input

    def validate_date(self, date):
        # Перевірка, чи дата відповідає правильному формату
        if not re.match(self.input_parser.date_pattern, date):
            print("Invalid date format. Please enter the date in the format DD/MM/YYYY.")
            return False
        return True
