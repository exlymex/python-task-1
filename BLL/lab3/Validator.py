import pyfiglet


class Validator:
    @staticmethod
    def validate_font(font):
        if font not in pyfiglet.FigletFont.getFonts():
            raise ValueError("Invalid font selected")

    @staticmethod
    def validate_color(color):
        valid_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        if color not in valid_colors:
            raise ValueError("Invalid color selected")
