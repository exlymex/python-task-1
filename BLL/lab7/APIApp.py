from colorama import Fore
from colorama import Style


class APIApp:
    def __init__(self, weather_api_client, reader_writer, validator, history, error_handler, results_display,
                 input_parser, data_saver):
        self.weather_api_client = weather_api_client
        self.reader_writer = reader_writer
        self.validator = validator
        self.history = history
        self.error_handler = error_handler
        self.results_display = results_display
        self.input_parser = input_parser
        self.data_saver = data_saver

    def get_weather_by_city(self, city):
        weather_data = self.weather_api_client.get_weather_by_city(city)
        if 'main' in weather_data:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            return {'temp': temp, 'feels_like': feels_like}
        return {}

    def get_wind_info(self, city):
        weather_data = self.weather_api_client.get_weather_by_city(city)
        if 'wind' in weather_data:
            return weather_data['wind']
        return {}

    def check_snow(self, city):
        weather_data = self.weather_api_client.get_weather_by_city(city)
        return 'snow' in weather_data

    def get_user_input(self):
        data_type = self.validator.validate_input("Enter the desired information ( temp, wind , is snowing): ",
                                                  ['phone', 'email', 'payment card', 'date'])
        user_input = self.reader_writer.read_input(f"Enter {data_type}: ")
        return data_type, user_input

    def run(self, data_type, city):
        try:
            # Task 1: Selecting the API provider
            data_from_api = None

            if data_type == '1':
                data_from_api = self.get_weather_by_city(city)
            elif data_type == '2':
                data_from_api = self.get_wind_info(city)
            elif data_type == '3':
                data_from_api = self.check_snow(city)

            # Adding the user's request and the result to the history
            self.history.add_to_history(city, (data_from_api))

            # Task 5: Displaying the results
            self.results_display.display_data(data_from_api, Fore.BLUE, Style.BRIGHT)

            # Task 6: Saving the data
            self.data_saver.save_data(data_from_api, 'json')

        except Exception as e:
            print(f"Error: {e}")
