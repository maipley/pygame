import pygame as pg
from objects import Paddle, Ball

win_x = 1280
win_y = 720
fps = 60

paddle_space = 15
paddle_width = win_x // 60
paddle_height = win_y // 4
paddle_center = (win_y // 2) - (paddle_height // 2)
paddle_speed = 12
paddle_color = "white"

ball_radius = win_x // 40
ball_speed = 8
ball_color = "white"

score_x = win_x // 5
score_y = win_y // 5
score_color = "white"

#print(f"[SCORE POSITION] X:{score_x}, Y:{score_y}")

pg.init()
clock = pg.time.Clock()

flags = pg.RESIZABLE #| pg.FULLSCREEN
win = pg.display.set_mode((win_x, win_y), flags)
pg.display.set_caption("Pong?")
font = pg.font.Font(None, 40)



def game():
    run = True
    global win, win_x, win_y
    l_point = False
    r_point = False
    
    paddle_left = Paddle(win, win_y, paddle_space, paddle_center, paddle_width, paddle_height, paddle_speed, paddle_color)
    paddle_right = Paddle(win, win_y, win_x - paddle_width - paddle_space, paddle_center, paddle_width, paddle_height, paddle_speed, paddle_color)
    ball = Ball(win, win_x, win_y, win_x // 2, win_y // 2, ball_radius, ball_speed, ball_color, 1, -1)

    paddle_list = [paddle_left, paddle_right]

    p_l_score, p_r_score = 0, 0
    p_l_yMult, p_r_yMult = 0, 0

    while run:
        
        win.fill("black")


        for event in pg.event.get():
            
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.VIDEORESIZE:
                #win = pg.display.set_mode(event.size, flags)
                win_x, win_y = event.size
            
        
        
        ## Keybinds
        keys = pg.key.get_pressed()
        
        esc = keys[pg.K_ESCAPE]
        p_l_up = keys[pg.K_w]
        p_l_down = keys[pg.K_s]
        p_r_up = keys[pg.K_o]
        p_r_down = keys[pg.K_l]

        if p_l_up and p_l_down:
            p_l_yMult = 0
        elif p_l_up:
            p_l_yMult = -1
        elif p_l_down:
            p_l_yMult = 1
        else:
            p_l_yMult = 0
        
        if p_r_up and p_r_down:
            p_r_yMult = 0
        elif p_r_up:
            p_r_yMult = -1
        elif p_r_down:
            p_r_yMult = 1
        else:
            p_r_yMult = 0

        if esc:
            run = False


        for paddle in paddle_list:
            #if pg.Rect.colliderect(ball.getRect(), paddle.getRect()):
                #ball.hit()
            if pg.Rect.colliderect(ball.getRect(), paddle_left.getRect()) and ball.getDir() == -1:
                ball.hit()
            if pg.Rect.colliderect(ball.getRect(), paddle_right.getRect()) and ball.getDir() == 1:
                ball.hit()


        paddle_left.update(p_l_yMult)
        paddle_right.update(p_r_yMult)
        point = ball.update()


        if point == -1:
            p_r_score += 1
        elif point == 1:
            p_l_score += 1
        if point:
            ball.reset(ball_speed)

        paddle_left.display()
        paddle_right.display()
        ball.display()
        #center_point = pg.draw.circle(win, "red", (win_x // 2, win_y // 2), 1)


        paddle_left.displayScore(p_l_score, score_x, score_y, font, score_color)
        paddle_right.displayScore(p_r_score, win_x - score_x, score_y, font, score_color)

        #print(p_l_score, p_r_score)

        pg.display.update()

        l_point, r_point = False, False

        clock.tick(fps)

    pg.quit()

if __name__ == "__main__":
    game()
