import pygame as pg
from CheckerBoard import CheckerBoard

print('Initializing pygame.')

pg.init()
pg.display.set_caption('Checkers')
win = pg.display.set_mode((800, 600))

checker_board = CheckerBoard()
square_size = 50
board_offset_x = 200
board_offset_y = 100

run = True
while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    for i, row in enumerate(checker_board.board):
        for j, square in enumerate(row):
            rect = (board_offset_x + i * square_size,
                    board_offset_y + j * square_size,
                    square_size, square_size)
            pg.draw.rect(win, square.color, rect)

    pg.display.update()

print('Game over.')
