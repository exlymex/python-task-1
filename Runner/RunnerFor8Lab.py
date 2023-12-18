from BLL.Lab8.DataProcessor import DataProcessor
from Shared.ReaderWriter import ReaderWriter
from Shared.Validator import Validator
from UI.Menu.MenuLab8 import MenuLab8


class RunnerLab8:
    @staticmethod
    def run():
        data_processor = DataProcessor()
        validator = Validator(None)
        reader_writer = ReaderWriter()
        menu = MenuLab8(data_processor, validator, reader_writer)
        menu.run()


if __name__ == "__main__":
    RunnerLab8.run()

