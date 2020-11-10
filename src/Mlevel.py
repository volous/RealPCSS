import pygame as pg
import numpy as np


class Level:

    def __init__(self, sizeX, sizeY, posX, posY, screen):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.screen = screen
        self.block_size = 32
        self.hit = False
        self.rect = None
        self.rectX = 0
        self.rectY = 0
        self.impassible_recX = 0
        self.impassible_recY = 0
        self.rect_array = []
        self.imp_array = []
        self.walkable = np.zeros((15, 15), dtype=bool)
        self.distance = 64
        self.white = (255, 255, 255)
        self.gray = (125, 125, 125)

    def level(self):
        map_size = 15
        for i in range(0, map_size):
            for j in range(0, map_size):
                self.rectX = 217 + i * self.block_size
                self.rectY = 117 + j * self.block_size
                rect = pg.Rect(self.rectX, self.rectY, self.block_size, self.block_size)
                self.rect_array.append(rect)
        self.walkable[1:-1, 1:-1] = True
        for i in range(1, 14):
            for j in range(1, 14):
                if i % 2 == 0 and j % 2 == 0:
                    self.walkable[i, j] = False

    def impassible_blocks(self):
        for i in range(0, 6):
            for j in range(0, 6):
                self.impassible_recX = 281 + i * self.distance
                self.impassible_recY = 181 + j * self.distance
                rect = pg.Rect(self.impassible_recX, self.impassible_recY, self.block_size, self.block_size)
                self.imp_array.append(rect)
        for i in range(0, 15):
            for j in range(0, 15):
                wall_rect_vert = pg.Rect(217 + i * self.block_size, 117 + j * 448, self.block_size, self.block_size)
                self.imp_array.append(wall_rect_vert)
                wall_rect_hori = pg.Rect(217 + i * 448, 117 + j * self.block_size, self.block_size, self.block_size)
                self.imp_array.append(wall_rect_hori)

    def draw_level(self):
        for i in self.rect_array:
            pg.draw.rect(self.screen, self.white, i)
        for i in self.imp_array:
            pg.draw.rect(self.screen, self.gray, i)


    # def positional_grid(self):
    #     # assigning a color for the rectangles
    #     black = (0, 0, 0)
    #     # setting the size of the rectangles
    #     block_size = self.block_size
    #     # setting the map_size
    #     map_size = 15
    #     # adding a 2D array to store the rectangles
    #     self.positional_array_bomb = np.ndarray([map_size, map_size], dtype=pg.Rect)
    #     # for loop that, creates a grid from start of level edge to the end
    #     for i in range(0, map_size):
    #         for j in range(0, map_size):
    #             self.rectX = 217 + i * block_size
    #             self.rectY = 117 + j * block_size
    #             # assigning a pygame function that draws a rectangle
    #             self.rect = pg.Rect(self.rectX, self.rectY, block_size, block_size)
    #             self.positional_array.append(self.rectX)
    #             self.positional_array_bomb[i, j] = [(self.rect.x + 16), (self.rect.y + 16)]
    #             # pg.draw.line(self.screen, blue, self.rect, 1)
    #             # using methods from pygame to draw a rectangle on the src screen,
    #             pg.draw.rect(self.screen, black, self.rect, 1)