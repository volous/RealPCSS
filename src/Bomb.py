import time
import pygame as pg
import threading


class Bomb:
    def __init__(self, explRad, pPosX, pPosY, bState, bReload, screen, walkable, index_x, index_y):
        self.explRad = explRad
        self.pPosX = pPosX+16
        self.pPosY = pPosY+16
        self.bState = bState
        self.bReload = bReload
        self.screen = screen
        self.placed = True
        self.secs = 3
        self.bomb_thread = threading.Thread(target=self.timer)
        self.bomb_thread.start()
        self.walkable = walkable
        self.index_x = index_x
        self.index_y = index_y


    def timer(self):
        time.sleep(self.secs)
        self.placed = False
        self.bomb_explode()

    def place_bomb(self):
        if self.placed:
            pg.draw.circle(self.screen, (255, 0, 0), (self.pPosX, self.pPosY), 16, 0)

    def bomb_explode(self):
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x + i, self.index_y]:
                pg.draw.circle(self.screen, (255, 0, 0), (self.pPosX + i * 32, self.pPosY), 16, 0)
            else:
                break
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x - i, self.index_y]:
                pg.draw.circle(self.screen, (255, 0, 0), (self.pPosX - i * 32, self.pPosY), 16, 0)
            else:
                break
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x, self.index_y + i]:
                pg.draw.circle(self.screen, (255, 0, 0), (self.pPosX, self.pPosY + i * 32), 16, 0)
            else:
                break
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x, self.index_y - i]:
                pg.draw.circle(self.screen, (255, 0, 0), (self.pPosX, self.pPosY - i * 32), 16, 0)
            else:
                break
