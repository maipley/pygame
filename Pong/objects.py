import pygame as pg

def speed_conv(x):
    new_speed = 5 + (x ** 0.65)
    return new_speed

class Paddle:
    def __init__(self, window, window_width, window_height, posx, posy, width, height, speed, color, right = False, paused = False):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.right = right
        self.paused = paused
        
        self.paddleRect = pg.Rect(posx, posy, self.width, self.height)
        self.paddle = pg.draw.rect(self.window, self.color, self.paddleRect)

    def display(self):
        self.paddle = pg.draw.rect(self.window, self.color, self.paddleRect)

    
    def update(self, yMult):
        if not self.paused:
            self.posy = self.posy + self.speed * yMult
            #print(self.posy)
            if self.posy < 0:
                self.posy = 0

            if self.posy + self.height >= self.window_height:
                self.posy = self.window_height - self.height

            self.paddleRect = (self.posx, self.posy, self.width, self.height) 


    def displayScore(self, score, font, color):
        x = self.window_width // 5
        y = self.window_height // 5
        if self.right:
            x = x * 4
        score = font.render(str(score), True, color)
        scoreRect = score.get_rect(center=(x, y))

        self.window.blit(score, scoreRect)


    def resize(self, window_width, window_height, width, height, paddle_space):
        self.window_width = window_width
        self.window_height = window_height
        self.width = width
        self.height = height
        self.posx = paddle_space
        if self.right:
            self.posx = self.window_width - self.width - paddle_space


    def pause(self):
        if not self.paused:
            print("pauseing")
            self.paused = True
        else:
            self.paused = False


    def getRect(self):
        return self.paddleRect




class Ball:
    def __init__(self, window, window_width, window_height, posx, posy, radius, base_speed, color, xMult, yMult, paused = False):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.base_speed = base_speed
        self.speed = speed_conv(base_speed)
        self.color = color
        self.xMult = xMult
        self.yMult = yMult
        self.ball = pg.draw.circle(self.window, self.color, (self.posx, self.posy), self.radius)
        self.justonce = True

        self.paused = paused


    def display(self):
        self.ball = pg.draw.circle(self.window, self.color, (self.posx, self.posy), self.radius)


    def update(self):
        if not self.paused:
            if self.posy - self.radius <= 0 and self.yMult == -1:
                self.yMult = 1
            if self.posy + self.radius >= self.window_height and self.yMult == 1:
                self.yMult = -1

            self.posx += self.speed * self.xMult
            self.posy += self.speed * self.yMult
        
            #print(self.justonce, self.posx, self.window_width)

            if (self.posx - self.radius) <= 0 and self.justonce:
                self.justonce = False
                return -1
            elif (self.posx + self.radius) >= self.window_width and self.justonce:
                self.justonce = False
                return 1
            else:
                return 0


    def reset(self, speed):
        self.posx = self.window_width // 2
        self.posy = self.window_height // 2

        self.xMult *= -1
        self.base_speed = speed
        self.speed = speed_conv(self.base_speed)
        self.justonce = True


    def hit(self):
        self.xMult *= -1
        #print(f"OLD {self.base_speed} || {self.speed}")
        self.base_speed += 1
        self.speed = speed_conv(self.base_speed)
        #print(f"NEW {self.base_speed} || {self.speed}")


    def resize(self, window_width, window_height, radius):
        self.window_width = window_width
        self.window_height = window_height
        self.radius = radius

    
    def pause(self):
        if not self.paused:
            self.paused = True
        else:
            self.paused = False

    def getRect(self):
        return self.ball


    def getDir(self):
        return self.xMult
