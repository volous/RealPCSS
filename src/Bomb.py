import time

import pygame as pg


class Bomb:

    # bRad is blastRadius
    def __init__(self, bRadX, bRadY, pPosX, pPosY, bState, bReload, screen):
        self.bRadX = bRadX
        self.bRadY = bRadY
        self.pPosX = pPosX
        self.pPosY = pPosY
        self.bState = bState
        self.bReload = bReload
        self.bomb_state_one = pg.image.load("Res/bomb1.png")
        pg.transform.scale(self.bomb_state_one, (32, 32))
        self.bomb_state_two = pg.image.load("Res/bomb2.png")
        pg.transform.scale(self.bomb_state_two, (32, 32))
        self.bomb_state_three = pg.image.load("Res/bomb3.png")
        pg.transform.scale(self.bomb_state_three, (32, 32))
        self.bomb_state = [self.bomb_state_one, self.bomb_state_two, self.bomb_state_three]
        self.screen = screen

        self.start_ticks = pg.time.get_ticks()
        self.ticks = 0




    def bomb(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    # self.screen.blit(self.bomb_state[0], (self.pPosX, self.pPosY))
                    self.rect = pg.Rect((self.pPosX, self.pPosY, 32, 32))
                    pg.draw.rect(self.screen, (255, 0, 0), self.rect)

