import pygame as pg


class Tile():

    def __init__(self, screen, color, walkable, explodable, visible, index_x, index_y):
        self.screen = screen
        self.color = color
        self.walkable = walkable
        self.explodable = explodable
        self.visible = visible
        self.index_x = index_x
        self.index_y = index_y
        self.blocksize = 32

    def draw(self):
        if self.visible:
            rect = pg.Rect(217 + self.index_x * self.blocksize, 117 + self.index_y * self.blocksize, self.blocksize, self.blocksize)
            pg.draw.rect(self.screen, self.color, rect)
        else:
            rect = pg.Rect(217 + self.index_x * self.blocksize, 117 + self.index_y * self.blocksize, self.blocksize,
                           self.blocksize)
            pg.draw.rect(self.screen, (255, 255, 255), rect)
            self.walkable = True