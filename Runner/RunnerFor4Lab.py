from SharedAccess.ascii_art_library import ascii_art
from UI.Menu.MenuLab4 import MenuLab4
from SharedAccess.ReaderWriter import ReaderWriter
from SharedAccess.Validator import Validator
from BLL.lab4.ASCIIArtGenerator import ASCIIArtGenerator


class Runner:
    def __init__(self):
        self.reader_writer = ReaderWriter()
        self.generator = ASCIIArtGenerator(ascii_art, self.reader_writer)
        self.validator = Validator(None)
        self.menu = MenuLab4(self.generator, self.reader_writer, self.validator)

    def run(self):
        self.menu.run()


if __name__ == "__main__":
    runner = Runner()
    runner.run()
