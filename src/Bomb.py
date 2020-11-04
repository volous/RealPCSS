import time
import Menu as m
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
        self.placed = False
        self.secs = 200

    def timer(self):
        try:
            while self.secs > 0:
                self.secs -= 1
        except:
            print("timer fail")



    def bomb(self, bombX, bombY):
        self.bombX = bombX
        self.bombY = bombY
        self.newX = 0
        self.newY = 0
        trigger = pg.key.get_pressed()
        print(self.secs)
        if trigger[pg.K_SPACE] and not self.placed:
                self.placed = True
                if self.placed:
                    self.newX = self.bombX
                    self.newY = self.bombY
                    self.screen.blit(self.bomb_state[0], (self.newX, self.newY))
                    self.timer()
                    if self.secs == 0:
                        self.placed = False
                        # self.secs = 200



