import pygame as pg

class Paddle:
    def __init__(self, window, posx, posy, width, height, speed, color):
        self.window = window
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        
        self.paddleRect = pg.Rect(posx, posy, width, height)
        self.paddle = pg.draw.rect(window, self.color, self.paddleRect)

    def display(self):
        self.paddle = pg.draw.rect(window, self.color, self.paddleRect)
    
    def update(self, yMult, window_height):
        self.posy = self.posy + self.speed * yMult

        if self.posy < 0:
            self.posy = 0

        if self.posy + self.height = window_height:
            self.posy = window_height - self.height

        self.paddleRect = (self.posx, self.posy, self.width, self.height) 


    def displayScore(self, score, x, y, color):
        score = pg.font.Font('freesansbold.ttf', 20).render(str(score), True, (255, 255, 255))
        scoreRect = score.get_rect()
        scoreRect.center = (x, y)


    def getRect():
        return self.paddleRect




class Ball:
    def __init__(self, window, psx, posy, radius, speed, color):
        self.window = window
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.xMul = 0
        self.yMul = 0
        self.ball = pg.draw.circle(window, self.color, (self.posx, self.posy), self.radius)
        self.justonce = 1

    def display(self):
        self.ball = pg.draw.circle(window, self.color, (self.posx, self.posy), self.radius)

    def update(self, window_width, window_height)
        
