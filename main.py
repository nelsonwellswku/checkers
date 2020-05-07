import pygame as pg
from CheckerBoard import CheckerBoard
from Palette import Gold

print('Initializing pygame.')

pg.init()
pg.display.set_caption('Checkers')
win = pg.display.set_mode((1024, 768))

checker_board = CheckerBoard()
square_size = 75
checker_size = 25
board_offset_x = 200
board_offset_y = 75

run = True
while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    outline_rect = (board_offset_x,
                    board_offset_y,
                    square_size * 8,
                    square_size * 8)
    pg.draw.rect(win, Gold, outline_rect, 15)

    for row_index, row in enumerate(checker_board.board):
        for col_index, square in enumerate(row):
            rect = (board_offset_x + col_index * square_size,  # left
                    board_offset_y + row_index * square_size,  # top
                    square_size, square_size)
            pg.draw.rect(win, square.color, rect)

            if(square.checker != None):
                circle_center = (
                    int(board_offset_x + (square_size / 2) +
                        col_index * square_size),
                    int(board_offset_y + (square_size / 2) +
                        row_index * square_size),
                )
                pg.draw.circle(win, square.checker.color,
                               circle_center, checker_size)
                pg.draw.circle(win, Gold,
                               circle_center, checker_size + 1, 1)

    pg.display.update()

print('Game over.')
