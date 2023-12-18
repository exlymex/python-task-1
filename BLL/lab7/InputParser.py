import json
import os
import re


# Class for handling user input and parsing
class InputParser:
    def __init__(self):
        with open(os.path.join('..', 'Config', 'default.json')) as f:
            data = json.load(f)
            self.date_pattern = data['patterns']['date']
            self.phone_pattern = data['patterns']['phone']
            self.email_pattern = data['patterns']['email']
            self.credit_card_pattern = data['patterns']['credit_card']


    def parse_user_input(self, user_input):
        date_tuples = re.findall(self.date_pattern, user_input)
        dates = ['/'.join(date_tuple) for date_tuple in date_tuples]
        phones = re.findall(self.phone_pattern, user_input)
        emails = [email.rstrip(',') for email in re.findall(self.email_pattern, user_input)]
        credit_cards = re.findall(self.credit_card_pattern, user_input)

        return dates, phones, emails, credit_cards

