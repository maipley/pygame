import pygame as pg


win_x = 800
win_y = 600

# INIT
pg.init()
clock = pg.time.Clock()
dt = 0
## SCREEN
win = pg.display.set_mode((win_x, win_y))
pg.display.set_caption("PyGame")

## PLAYER
pos_x = 0
pos_y = 0
size = 10
vel = 8
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            print("Exiting...")

    window.fill("black")

    ## SQUARE
    pos = pg.Rect(pos_x - (size / 2), pos_y - (size / 2), size, size)
    sqr = pg.draw.rect(win, "green", pos)

    ## KEYS
    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        running = False

    if keys[pg.K_w]:
        if pos_y > 0:
            print("w")
            pos_y -= vel
        #if size < 100:
        #    size += 1
    if keys[pg.K_a]:
        if pos_x > 0:
            print("a")
            pos_x -= vel
    if keys[pg.K_s]: 
        if pos_y < window_y:
            print("s")
            pos_y += vel
        #if size > 1:
        #    size -= 1
    if keys[pg.K_d]:
        if pos_x < window_x:
            print("d")
            pos_x += vel
    

    pg.display.flip()
    pg.display.update()
    clock.tick(120)

print("Out of loop")
pg.quit()
