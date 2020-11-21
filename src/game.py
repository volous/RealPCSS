import const
from character import Character
from mlevel import Level
import pygame as pg
import time
from _thread import *
import pickle
import socket
from client import Client
from server import Server


class Game_handler:

    def __init__(self, screen, client, up, down, left, right, plant_bomb):
        # Initialize level, characters
        self.screen = screen
        self.client = client
        # an empty array that tracks bombs and their explosions
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.plant_bomb = plant_bomb
    # method that draws the level and keeps track of the actions for the player and bombs
    def draw(self):
        self.client.level.draw()
        for c in self.client.characters:
            c.draw()
        for b in self.client.bombs:
            b.draw(time.time())

        # self.actions()
        # self.bomb_actions()


    def move(self):
        trigger = pg.key.get_pressed()
        if trigger[self.up]:
            self.client.send(const.CLIENT_MOVE_UP)
        elif trigger[self.down]:
            self.client.send(const.CLIENT_MOVE_DOWN)
        elif trigger[self.left]:
            self.client.send(const.CLIENT_MOVE_LEFT)
        elif trigger[self.right]:
            self.client.send(const.CLIENT_MOVE_RIGHT)
        elif trigger[self.plant_bomb]:
            self.client.send(const.CLIENT_PLANT_BOMB)
    # # method that draws the bomb and the bombs explosion for each character
    # def bomb_actions(self):
    #     for b in self.bombs:
    #         if not b.placed:
    #             b.bomb_explode(self.level.tile_array)
    #             chars = [c for c in self.player if c.PLAYER_ID == b.PLAYER_ID]
    #             # if bomb is no longer placed reduce bomb_count
    #             chars[0].bomb_count -= 1
    #             self.player = [c for c in self.player if not c.check_death(b)]
    #             self.bombs.remove(b)
    #         else:
    #             b.draw_bomb(time.time())
    #
    # # method that keeps track of what actions a player can perform
    # def actions(self):
    #     # for each c in characters draw a character
    #     for c in self.player:
    #         can_place = True
    #         for b in self.bombs:
    #             # if a player objects x and y index is inside the bombs x and y index the player objects are not allowed
    #             # to place a bomb
    #             if b.index_x == c.index_x and b.index_y == c.index_y:
    #                 can_place = False
    #         bomb = c.player_actions(can_place, self.level.tile_array)
    #         # if the bomb object exists then increase the count of bombs and append it to bombs list
    #         if bomb is not None:
    #             self.bombs.append(bomb)
    #             c.bomb_count += 1
    #         # draw each character
    #         c.draw()
