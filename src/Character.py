import pygame as pg

size = width, height = 900, 700

class Character:
    def __init__(self, posX, posY, screen):
        self.posX = posX
        self.posY = posY
        self.width  = 32
        self.height = 32
        self.vel = 32
        self.screen = screen
        self.rect = pg.Rect

    def draw_char(self):
        screen = self.screen
        self.rect = pg.Rect((self.posX, self.posY, self.width, self.height))
        pg.draw.rect(screen, (255, 0, 0), self.rect)


    def player_movement(self):
        trigger = pg.key.get_pressed()
        if trigger[pg.K_w] and self.posY > self.vel:
            self.posY -= self.vel
        if trigger[pg.K_s] and self.posY + self.vel + self.height < height:
            self.posY += self.vel
        if trigger[pg.K_a] and self.posX > self.vel:
            self.posX -= self.vel
        if trigger[pg.K_d] and self.posX + self.vel + self.width < width:
            self.posX += self.vel

