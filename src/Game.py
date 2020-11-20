import player_id
from Character import Character
from Mlevel import Level
import pygame as pg
import time
from _thread import *
import pickle
import socket
from Network import Network


class Game_handler:

    def __init__(self, screen):
        # Initialize level, characters
        self.screen = screen
        self.level = Level(self.screen)

        self.char1 = Character(3, player_id.PLAYER_ONE_ID, 1, 1, self.screen,
                               (255, 0, 0), pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_SPACE)

        self.char2 = Character(3, player_id.PLAYER_TWO_ID, 13, 1, self.screen,
                               (0, 255, 0), pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_k)

        self.characters = [self.char1, self.char2]
        # an empty array that tracks bombs and their explosions
        self.bombs = []
        self.n = Network()
        self.p = self.n.getP()


    # method that draws the level and keeps track of the actions for the player and bombs
    def draw(self):
        self.level.draw()
        self.actions()
        self.bomb_actions()
        # self.p.action()
        # self.p.bomb_actions()
        # p2 = self.n.send(self.p)

    # method that draws the bomb and the bombs explosion for each character
    def bomb_actions(self):
        for b in self.bombs:
            if not b.placed:
                b.bomb_explode(self.level.tile_array)
                chars = [c for c in self.characters if c.PLAYER_ID == b.PLAYER_ID]
                # if bomb is no longer placed reduce bomb_count
                chars[0].bomb_count -= 1
                self.characters = [c for c in self.characters if not c.check_death(b)]
                self.bombs.remove(b)
            else:
                b.draw_bomb(time.time())

    # method that keeps track of what actions a player can perform
    def actions(self):
        # for each c in characters draw a character
        for c in self.characters:
            can_place = True
            for b in self.bombs:
                # if a player objects x and y index is inside the bombs x and y index the player objects are not allowed
                # to place a bomb
                if b.index_x == c.index_x and b.index_y == c.index_y:
                    can_place = False
            bomb = c.player_actions(can_place, self.level.tile_array)
            # if the bomb object exists then increase the count of bombs and append it to bombs list
            if bomb is not None:
                self.bombs.append(bomb)
                c.bomb_count += 1
            # draw each character
            c.draw()
