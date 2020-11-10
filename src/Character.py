import pygame as pg
from Bomb import Bomb


class Character:
    def __init__(self, index_x, index_y, posX, posY, screen, walkable, player_color):
        self.index_x = index_x
        self.index_y = index_y
        self.posX = posX
        self.posY = posY
        self.width = 32
        self.height = 32
        self.vel = 32
        self.rect = pg.Rect
        self.screen = screen
        self.bombs = []
        self.walkable = walkable
        self.player_color = player_color

    def draw_char(self):
        self.rect = pg.Rect((self.posX, self.posY, self.width, self.height))
        pg.draw.rect(self.screen, (255, 0, 0), self.rect)
        for i in self.bombs:
            if i.placed:
                i.place_bomb()
            else:
                self.bombs.remove(i)

    def player_actions(self):
        trigger = pg.key.get_pressed()
        if trigger[pg.K_w] and self.index_y > 0 and self.walkable[self.index_x, self.index_y-1]:
            self.posY -= self.vel
            self.index_y -= 1
        if trigger[pg.K_s] and self.index_y < 14 and self.walkable[self.index_x, self.index_y+1]:
            self.posY += self.vel
            self.index_y += 1
        if trigger[pg.K_a] and self.index_x > 0 and self.walkable[self.index_x-1, self.index_y]:
            self.posX -= self.vel
            self.index_x -= 1
        if trigger[pg.K_d] and self.index_x < 14 and self.walkable[self.index_x+1, self.index_y]:
            self.posX += self.vel
            self.index_x += 1
        if trigger[pg.K_SPACE]:
            self.bombs.append(Bomb(3, self.posX, self.posY, True, True, self.screen, self.walkable, self.index_x, self.index_y))
