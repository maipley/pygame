import pygame as pg

win_x, win_y = 1280, 720

pg.init()
win = pg.display.set_mode((win_x, win_y))

run = True
while run:
    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                run = False


pg.quit()
