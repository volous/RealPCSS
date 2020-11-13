import time
import pygame as pg
import threading

class Bomb:
    def __init__(self, PLAYER_ID, explRad, pPosX, pPosY, bState, bReload, screen, walkable, index_x, index_y, color):
        self.PLAYER_ID = PLAYER_ID
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
        self.color = color
        self.list = []

    def timer(self):
        while self.secs > 0:
            font = pg.font.Font('freesansbold.ttf', 20)
            text = font.render(str(self.secs), True, (255, 255, 255), self.color)
            self.screen.blit(text, (self.pPosX-6, self.pPosY-10))
            time.sleep(1)
            self.secs -= 1
        self.placed = False
        self.bomb_explode()

    def draw_bomb(self):
        if self.placed:
            pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY), 16, 0)

    def bomb_explode(self):
        self.list = [(self.index_x, self.index_y)]
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x + i, self.index_y]:
                pg.draw.circle(self.screen, self.color, (self.pPosX + i * 32, self.pPosY), 16, 0)
                self.list.append((self.index_x + i, self.index_y))
            else:
                break
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x - i, self.index_y]:
                pg.draw.circle(self.screen, self.color, (self.pPosX - i * 32, self.pPosY), 16, 0)
                self.list.append((self.index_x - i, self.index_y))
            else:
                break
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x, self.index_y + i]:
                pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY + i * 32), 16, 0)
                self.list.append((self.index_x, self.index_y + i))
            else:
                break
        for i in range(1, self.explRad+1):
            if self.walkable[self.index_x, self.index_y - i]:
                pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY - i * 32), 16, 0)
                self.list.append((self.index_x, self.index_y - i))
            else:
                break
