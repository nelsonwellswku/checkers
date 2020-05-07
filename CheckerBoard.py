red = (255, 0, 0)
green = (0, 255, 0)
black = (255, 255, 255)
white = (0, 0, 0)


def _generate_empty_row(color_one, color_two):
    return [Square(color_one, None) if x % 2 != 0 else Square(color_two, None) for x in range(8)]


class Checker:
    def __init__(self, color):
        self.color = color
        self.isKing = False


class Square:
    def __init__(self, color, checker):
        self.color = color
        self.checker = checker


class CheckerBoard:
    def __init__(self):
        self.board = [
            _generate_empty_row(white, black),
            _generate_empty_row(black, white),
            _generate_empty_row(white, black),
            _generate_empty_row(black, white),
            _generate_empty_row(white, black),
            _generate_empty_row(black, white),
            _generate_empty_row(white, black),
            _generate_empty_row(black, white),
        ]
