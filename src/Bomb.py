import time
import pygame as pg

class Bomb:
    def __init__(self, PLAYER_ID, explRad, pPosX, pPosY, bState, bReload, screen, index_x, index_y, color):
        self.PLAYER_ID = PLAYER_ID
        self.explRad = explRad
        self.pPosX = pPosX+16
        self.pPosY = pPosY+16
        self.bState = bState
        self.bReload = bReload
        self.screen = screen
        self.placed = True
        self.sec = time.time()
        self.time_max = 3
        self.index_x = index_x
        self.index_y = index_y
        self.color = color
        self.list = []

    def draw_bomb(self, secs):
        boom = int(secs - self.sec)
        if boom == self.time_max:
            self.placed = False
        if self.placed:
            pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY), 16, 0)
            font = pg.font.Font('freesansbold.ttf', 20)
            text = font.render(str(boom), True, (255, 255, 255), self.color)
            self.screen.blit(text, (self.pPosX-6, self.pPosY-10))

    def bomb_explode(self, tile_array):
        self.list = [(self.index_x, self.index_y)]
        for i in range(1, self.explRad+1):
            if tile_array[self.index_x + i, self.index_y].walkable:
                pg.draw.circle(self.screen, self.color, (self.pPosX + i * 32, self.pPosY), 16, 0)
                self.list.append((self.index_x + i, self.index_y))
            elif tile_array[self.index_x + i, self.index_y].explodable:
                pg.draw.circle(self.screen, self.color, (self.pPosX + i * 32, self.pPosY), 16, 0)
                self.list.append((self.index_x + i, self.index_y))
                tile_array[self.index_x + i, self.index_y].visible = False
                tile_array[self.index_x + i, self.index_y].walkable = True
                break
            else:
                break
        for i in range(1, self.explRad+1):
            if tile_array[self.index_x - i, self.index_y].walkable:
                pg.draw.circle(self.screen, self.color, (self.pPosX - i * 32, self.pPosY), 16, 0)
                self.list.append((self.index_x - i, self.index_y))
            elif tile_array[self.index_x - i, self.index_y].explodable:
                pg.draw.circle(self.screen, self.color, (self.pPosX - i * 32, self.pPosY), 16, 0)
                self.list.append((self.index_x - i, self.index_y))
                tile_array[self.index_x - i, self.index_y].visible = False
                tile_array[self.index_x - i, self.index_y].walkable = True
                break
            else:
                break
        for i in range(1, self.explRad+1):
            if tile_array[self.index_x, self.index_y + i].walkable:
                pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY + i * 32), 16, 0)
                self.list.append((self.index_x, self.index_y + i))
            elif tile_array[self.index_x, self.index_y + i].explodable:
                pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY + i * 32), 16, 0)
                self.list.append((self.index_x, self.index_y + i))
                tile_array[self.index_x, self.index_y + i].visible = False
                tile_array[self.index_x, self.index_y + i].walkable = True
                break
            else:
                break
        for i in range(1, self.explRad+1):
            if tile_array[self.index_x, self.index_y - i].walkable:
                pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY - i * 32), 16, 0)
                self.list.append((self.index_x, self.index_y - i))
            elif tile_array[self.index_x, self.index_y - i].explodable:
                pg.draw.circle(self.screen, self.color, (self.pPosX, self.pPosY - i * 32), 16, 0)
                self.list.append((self.index_x, self.index_y - i))
                tile_array[self.index_x, self.index_y - i].visible = False
                tile_array[self.index_x, self.index_y - i].walkable = True
                break
            else:
                break
