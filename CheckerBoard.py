from Palette import Black, White, Red, Green


def _generate_row(color_one, color_two, checker_one=None, checker_two=None):
    return [Square(color_one, checker_one) if x % 2 == 0 else Square(color_two, checker_two) for x in range(8)]


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
            _generate_row(Black, White, Checker(Green)),
            _generate_row(White, Black, None, Checker(Green)),
            _generate_row(Black, White, Checker(Green)),
            _generate_row(White, Black),
            _generate_row(Black, White),
            _generate_row(White, Black, None, Checker(Red)),
            _generate_row(Black, White, Checker(Red)),
            _generate_row(White, Black, None, Checker(Red))
        ]
