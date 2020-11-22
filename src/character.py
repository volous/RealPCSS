import pygame as pg
from bomb import Bomb


class Character:
    def __init__(self, max_bombs, PLAYER_ID, index_x, index_y, screen, player_color):
        self.bomb_count = 0
        self.max_bombs = max_bombs
        self.PLAYER_ID = PLAYER_ID
        self.index_x = index_x
        self.index_y = index_y
        self.width = 32
        self.height = 32
        self.rect = pg.Rect
        self.screen = screen
        self.bombs = []
        self.player_color = player_color
        self.alive = True
        self.explRad = 3

    # method that draws the basic character
    def draw(self):
        # if statement that checks if the boolean variable alive is true
        if self.alive:
            # sets rect to be a pg.Rect, which is a rectangle
            self.rect = pg.Rect((self.index_x * 32 + 217, self.index_y * 32 + 117, self.width, self.height))
            # draws the rectangle
            pg.draw.rect(self.screen, self.player_color, self.rect)

    # method that allows to check whether a player is alive or dead
    def check_death(self, bomb):
        # if statement that checks whether the index_x and y is inside of a list of bombs
        if (self.index_x, self.index_y) in bomb.list:
            # if index_ and y is inside of the bomb list it will set the boolean alive to false and remove the player(s)
            # that are inside of the bomb list
            self.alive = False
            return True
        return False

    # method that handles how many bombs the player(s) are allowed to place,
    # as long as bombs placed are lower than max_bombs
    def bomb_handler(self):
        print("trying to plant bomb")
        if self.bomb_count < self.max_bombs:
            print("succeeded")
            return Bomb(self.PLAYER_ID, self.explRad, True, True, self.screen,
                        self.index_x, self.index_y, self.player_color)
        else:
            return None
