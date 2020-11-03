import time
import pygame as pg


class Bomb:

    # bRad is blastRadius
    def __init__(self, bRadX, bRadY, bState, bReload, screen):
        self.bRadX = bRadX
        self.bRadY = bRadY
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
        # sets secs to be equal to bSecs
        print("boom")

    # timer method
    def timer(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if pg.KEYDOWN == pg.K_SPACE:
                        self.start_ticks
                        print(self.start_ticks)
                        self.ticks += 1
                        print(self.ticks)

