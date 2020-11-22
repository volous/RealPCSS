import time
import pygame as pg


class Bomb:
    def __init__(self, PLAYER_ID, explRad, bState, bReload, screen, index_x, index_y, color):
        self.PLAYER_ID = PLAYER_ID
        self.explRad = explRad
        self.bState = bState
        self.bReload = bReload
        self.screen = screen
        self.is_live = True
        self.plant_time = time.time()
        self.time_max = 3
        self.index_x = index_x
        self.index_y = index_y
        self.color = color
        self.list = []

    # method for handling bomb explosion
    def is_exploding(self, curr_time):
        boom = int(curr_time - self.plant_time)
        if boom >= self.time_max:
            self.is_live = False
            return True
        else:
            return False

    # method for drawing bombs, also keeps track of when the bomb should explode
    def draw(self, curr_time):
        boom = int(curr_time - self.plant_time)
        if boom == self.time_max:
            self.is_live = False
        # if the boolean placed is true then draw a bomb on the players position and text that counts up to
        # 3 and then explodes
        if self.is_live:
            pg.draw.circle(self.screen, self.color, (self.index_x * 32 + 217 + 16, self.index_y * 32 + 117 + 16), 16, 0)
            font = pg.font.Font('freesansbold.ttf', 20)
            text = font.render(str(boom), True, (255, 255, 255), self.color)
            self.screen.blit(text, (self.index_x * 32 + 217 + 8, self.index_y * 32 + 117 + 8))

    # methods for handling bomb explosion in client
    def bomb_explode_client(self, explosion_list):
        for index_x, index_y in explosion_list:
            pg.draw.circle(self.screen, self.color, (index_x * 32 + 217 + 16,
                                                     index_y * 32 + 117 + 16), 16, 0)

    # method for the explosion of the bombs
    def bomb_explode(self, tile_array):
        self.list = [(self.index_x, self.index_y)]
        for i in range(1, self.explRad + 1):
            # if the tile is walkable the bomb is allowed to explode further
            if tile_array[self.index_x + i, self.index_y].walkable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x + i, self.index_y))
            # if the tile is explodable it will stop the explosion on that tile by breaking on that tile
            elif tile_array[self.index_x + i, self.index_y].explodable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x + i, self.index_y))
                # sets the tile to be no longer visible and is walkable
                tile_array[self.index_x + i, self.index_y].visible = False
                tile_array[self.index_x + i, self.index_y].walkable = True
                break
            else:
                break
        for i in range(1, self.explRad + 1):
            # if the tile is walkable the bomb is allowed to explode further
            if tile_array[self.index_x - i, self.index_y].walkable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x - i, self.index_y))
            # if the tile is explodable it will stop the explosion on that tile by breaking on that tile
            elif tile_array[self.index_x - i, self.index_y].explodable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x - i, self.index_y))
                # sets the tile to be no longer visible and is walkable
                tile_array[self.index_x - i, self.index_y].visible = False
                tile_array[self.index_x - i, self.index_y].walkable = True
                break
            else:
                break
        for i in range(1, self.explRad + 1):
            # if the tile is walkable the bomb is allowed to explode further
            if tile_array[self.index_x, self.index_y + i].walkable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x, self.index_y + i))
            # if the tile is explodable it will stop the explosion on that tile by breaking on that tile
            elif tile_array[self.index_x, self.index_y + i].explodable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x, self.index_y + i))
                # sets the tile to be no longer visible and is walkable
                tile_array[self.index_x, self.index_y + i].visible = False
                tile_array[self.index_x, self.index_y + i].walkable = True
                break
            else:
                break
        for i in range(1, self.explRad + 1):
            # if the tile is walkable the bomb is allowed to explode further
            if tile_array[self.index_x, self.index_y - i].walkable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x, self.index_y - i))
            # if the tile is explodable it will stop the explosion on that tile by breaking on that tile
            elif tile_array[self.index_x, self.index_y - i].explodable:
                # appends the index's of a bombs explosion to a list
                self.list.append((self.index_x, self.index_y - i))
                # sets the tile to be no longer visible and is walkable
                tile_array[self.index_x, self.index_y - i].visible = False
                tile_array[self.index_x, self.index_y - i].walkable = True
                break
            else:
                break
