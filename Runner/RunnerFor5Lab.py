from SharedAccess.ReaderWriter import ReaderWriter
from SharedAccess.Validator import Validator
from UI.Menu.MenuLab5 import Menu5Lab


class Runner5Lab:
    def __init__(self):
        self.reader_writer = ReaderWriter()
        self.validator = Validator(input_parser = None)
        self.menu = Menu5Lab(self.reader_writer, self.validator)

    def run(self):
        self.menu.run()

if __name__ == "__main__":
    runner = Runner5Lab()
    runner.run()

