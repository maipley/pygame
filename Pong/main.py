import pygame as pg


win_x = 800
win_y = 600
font = pg.font.Font('freesansbold.ttf', 20)

pg.init()
clock = pg.time.Clock()

win = pg.display
win.set_mode((win_x, win_y))
win.set_caption("Pong?")


def game():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False


pg.quit()
