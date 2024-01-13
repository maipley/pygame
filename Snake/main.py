import pygame as pg
import random as rnd


GRID_SIZE = 20
SQR_SIZE = 40
FPS = 10

NONE = (0, 0)
UP = (0, -1)
LEFT = (-1, 0)
DOWN = (0, 1)
RIGHT = (1, 0)

SNAKE_LENGTH = 2
SNAKE_DIR = NONE
MAX_FOOD = 2

pg.init()
win = pg.display.set_mode((GRID_SIZE * SQR_SIZE, GRID_SIZE * SQR_SIZE))
pg.display.set_caption("Snake?")
clock = pg.time.Clock()


def main():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

    snk_head = (rnd.randint(1, GRID_SIZE - 2), rnd.randint(1, GRID_SIZE - 2))
    grid[snk_head[0]][snk_head[1]] = 1
    snk_list = [snk_head]
    snk_length = SNAKE_LENGTH
    snk_dir = SNAKE_DIR
    food_count = 0

    running = True
    dead = False
    while running:
        if dead:
            grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
            snk_head = (rnd.randint(1, GRID_SIZE - 2), rnd.randint(1, GRID_SIZE - 2))
            grid[snk_head[0]][snk_head[1]] = 1
            snk_list = [snk_head]
            snk_length = SNAKE_LENGTH
            snk_dir = SNAKE_DIR
            food_count = 0
            dead = False

        ## EVENT HANDLING ##
        for event in pg.event.get():
            match event.type:
                case pg.QUIT:
                    running = False
                case pg.KEYUP:
                    match event.key:
                        case pg.K_ESCAPE:
                            running = False
                        case pg.K_SPACE:
                            dead = True
                case pg.KEYDOWN:
                    match event.key:
                        case pg.K_w | pg.K_UP:
                            if snk_dir != DOWN:
                                snk_dir = UP
                        case pg.K_a | pg.K_LEFT:
                            if snk_dir != RIGHT:
                                snk_dir = LEFT
                        case pg.K_s | pg.K_DOWN:
                            if snk_dir != UP:
                                snk_dir = DOWN
                        case pg.K_d | pg.K_RIGHT:
                            if snk_dir != LEFT:
                                snk_dir = RIGHT

        ## UPDATE ##

        # SNAKE #
        snk_x = snk_head[0] + snk_dir[0]
        snk_y = snk_head[1] + snk_dir[1]
        if not 0 <= snk_x <= GRID_SIZE - 1 or not 0 <= snk_y <= GRID_SIZE - 1:
            dead = True
            continue
        elif grid[snk_x][snk_y] == 1 and snk_length > 2:
            dead = True
            continue
        elif grid[snk_x][snk_y] == 2:
            snk_length += 1
            food_count -= 1
        snk_head = (snk_x, snk_y)
        snk_list.insert(0, snk_head)

        if len(snk_list) > snk_length:
            popped = snk_list.pop()
            grid[popped[0]][popped[1]] = 0

        # FOOD #
        if food_count < MAX_FOOD:
            food_x = rnd.randint(0, GRID_SIZE - 1)
            food_y = rnd.randint(0, GRID_SIZE - 1)
            if grid[food_x][food_y] == 0:
                food_count += 1
                grid[food_x][food_y] = 2

        for x in snk_list:
            grid[x[0]][x[1]] = 1

        ## DRAW ##
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                match grid[x][y]:
                    case 1:
                        color = "green"
                    case 2:
                        color = "red"
                    case _:
                        color = "black"

                pg.draw.rect(
                    win, color, (x * SQR_SIZE, y * SQR_SIZE, SQR_SIZE, SQR_SIZE)
                )
                pg.draw.rect(
                    win, "#090909", (x * SQR_SIZE, y * SQR_SIZE, SQR_SIZE, SQR_SIZE), 1
                )

        pg.display.update()

        clock.tick(FPS)

    pg.quit()


if __name__ == "__main__":
    main()
