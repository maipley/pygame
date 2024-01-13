import pygame as pg
import random

win_x, win_y = 800, 400

GRID_SIZE = 10  # Grid size for example 10x10
GRID_SQR_SIZE = 50  # Size of each square in the grid in px

pg.init()
main_win = pg.display.set_mode((GRID_SIZE * GRID_SQR_SIZE, GRID_SIZE * GRID_SQR_SIZE))


def grid_random(lst):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            lst[y][x] = random.randint(0, 1)



def main():

    grid_list = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    # grid_random(grid_list)

    run = True
    while run:
        main_win.fill("black")

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                sqr_x = x // GRID_SQR_SIZE
                sqr_y = y // GRID_SQR_SIZE
                if grid_list[sqr_y][sqr_x] == 0:
                    grid_list[sqr_y][sqr_x] = 1
                else:
                    grid_list[sqr_y][sqr_x] = 0

        ## DRAW THE GRID
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                match grid_list[y][x]:
                    case 1:
                        color = "green"
                    case _:
                        color = "black"

                pg.draw.rect(main_win, color, (x * GRID_SQR_SIZE, y * GRID_SQR_SIZE, GRID_SQR_SIZE, GRID_SQR_SIZE))

        pg.display.update()

    pg.quit()

if __name__ == "__main__":
    main()
