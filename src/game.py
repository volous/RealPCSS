import const
import pygame as pg
import time


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