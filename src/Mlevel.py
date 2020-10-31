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
        self.im_recX = 0
        self.im_recY = 0
        self.positional_array = []
        self.im_rect_array = []
        self.im_rect_hor_array = []
        self.im_rect_ver_array = []

    # level
    def level(self):
        # assigning a color
        white = (255, 255, 255)
        pg.draw.rect(self.screen, white, (217, 117, 480, 480))

    # position grid
    def positional_grid(self):
        # assigning a color for the rectangles
        black = (0, 0, 0)
        blue = (0, 0, 255)
        # setting the size of the rectangles
        block_size = self.block_size
        # setting the map_size
        map_size = 15
        # adding a 2D array to store the rectangles
        self.positional_array_bomb = np.ndarray([map_size, map_size], dtype=pg.Rect)
        # for loop that, creates a grid from start of level edge to the end
        for i in range(0, map_size):
           for j in range(0, map_size):
                self.rectX = 217 + i * block_size
                self.rectY = 117 + j * block_size
                # assigning a pygame function that draws a rectangle
                self.rect = pg.Rect(self.rectX, self.rectY, block_size, block_size)
                self.positional_array.append(self.rectX)
                self.positional_array_bomb[i, j] = [(self.rect.x + 16), (self.rect.y + 16)]
                # pg.draw.line(self.screen, blue, self.rect, 1)
                # using methods from pygame to draw a rectangle on the src screen,
                pg.draw.rect(self.screen, black, self.rect, 1)
                # print(self.positional_array[0])
    def impassible_blocks(self):
        grey = (125, 125, 125)
        distance = 64
        block_size = self.block_size
        for i in range(0, 6):
            for j in range(0, 6):
                self.im_recX = 281 + i * distance
                self.im_recY = 181 + j * distance
                rect = pg.Rect(self.im_recX, self.im_recY, block_size, block_size)
                self.im_rect_array.append(rect.x)
                pg.draw.rect(self.screen, grey, rect, 0)

        for i in range(0, 15):
            for j in range(0, 15):
                wall_rect_vert = pg.Rect(217 + i * block_size, 117 + j * 448, block_size, block_size)
                self.im_rect_ver_array.append(wall_rect_vert)
                pg.draw.rect(self.screen, grey, wall_rect_vert, 0)
                wall_rect_hori = pg.Rect(217 + i * 448, 117 + j * block_size, block_size, block_size)
                self.im_rect_hor_array.append(wall_rect_hori)
                pg.draw.rect(self.screen, grey, wall_rect_hori)