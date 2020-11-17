import numpy as np
from Tile import Tile


class Level:

    def __init__(self, screen):
        # Initialize variables
        self.screen = screen
        self.tile_array = np.ndarray((15, 15), dtype=Tile)
        self.white = (255, 255, 255)
        self.gray = (125, 125, 125)
        self.orange = (200, 100, 0)
        self.make_tiles()
        self.destroyable_blocks()
        self.impassible_blocks()

    def make_tiles(self):
        for i in range(0, 15):
            for j in range(0, 15):
                self.tile_array[i, j] = Tile(self.screen, self.white, True, False, True, i, j)

    def destroyable_blocks(self):
        for i in range(1, 14):
            for j in range(1, 14):
                if (i > 2 or j > 2) and (i < 12 or j < 12) and (i > 2 or j < 12) and (i < 12 or j > 2):
                    if i % 2 != 0 or j % 2 != 0:
                        self.tile_array[i, j].explodable = True
                        self.tile_array[i, j].walkable = False
                        self.tile_array[i, j].color = self.orange



    def impassible_blocks(self):
        for i in range(0, 15):
            for j in range(0, 15):
                if i % 2 == 0 and j % 2 == 0:
                    if i > 0 and j > 0:
                        self.tile_array[i, j].walkable = False
                        self.tile_array[i, j].color = self.gray
                if i == 0 or j == 0 or j == 14 or i == 14:
                    self.tile_array[i, j].walkable = False
                    self.tile_array[i, j].color = self.gray

    def draw(self):
        for i in self.tile_array:
            for j in i:
                j.draw()
