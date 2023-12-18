# Клас для запуску програми
from BLL.lab7.APIApp import APIApp
from BLL.lab7.DataSaver import DataSaver
from BLL.lab7.InputParser import InputParser
from BLL.lab7.WeatherAPIClient import WeatherAPIClient
from SharedAccess.ReaderWriter import ReaderWriter
from SharedAccess.Validator import Validator
from BLL.lab7.History import History
from BLL.lab7.ErrorHandler import ErrorHandler
from BLL.lab7.ResultsDisplay import ResultsDisplay
from UI.Menu.MenuLab7 import MenuLab7


class RunnerLab7:
    def run_program(self):
        api_key = "49d965b7ac6933d5cc545a73b1751b78"
        weather_api_client = WeatherAPIClient(api_key)

        reader_writer = ReaderWriter()
        input_parser = InputParser()  # Creating an instance of the InputParser class
        validator = Validator(input_parser)  # Passing the instance of the InputParser class to the Validator class
        history = History()
        error_handler = ErrorHandler()
        results_display = ResultsDisplay()
        data_saver = DataSaver()

        api_app = APIApp(weather_api_client, reader_writer, validator, history, error_handler, results_display, input_parser,
                         data_saver)

        menu_lab7 = MenuLab7(api_app, validator, reader_writer)
        menu_lab7.run()


if __name__ == "__main__":
    RunnerLab7().run_program()


