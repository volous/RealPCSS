import pygame as pg

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