import pygame as pg
from Bomb import Bomb


class Character:
    # init
    def __init__(self, max_bombs, PLAYER_ID, index_x, index_y, screen, player_color, up, down, left, right,
                 place_bomb):
        # initializing variables
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
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.place_bomb = place_bomb
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
            # redundant will be removed
            font = pg.font.Font('freesansbold.ttf', 10)
            text = font.render(str((self.index_x * 32 + 217, self.index_y * 32 + 117)), True, (255, 255, 255), (0, 0, 0))
            self.screen.blit(text, (self.index_x * 32 + 217, self.index_y * 32 + 117))

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
        if self.bomb_count < self.max_bombs:
            return Bomb(self.PLAYER_ID, self.explRad, True, True, self.screen,
                        self.index_x, self.index_y, self.player_color)

    # method that handles player actions such as movement, and bomb placement.
    # checks which key has been pressed and if the tile they are trying to move into is walkable
    def player_actions(self, can_place, tiles):
        trigger = pg.key.get_pressed()
        if trigger[self.up] and self.index_y > 0 and tiles[self.index_x, self.index_y - 1].walkable:
            self.index_y -= 1
        elif trigger[self.down] and self.index_y < 14 and tiles[self.index_x, self.index_y + 1].walkable:
            self.index_y += 1
        elif trigger[self.left] and self.index_x > 0 and tiles[self.index_x - 1, self.index_y].walkable:
            self.index_x -= 1
        elif trigger[self.right] and self.index_x < 14 and tiles[self.index_x + 1, self.index_y].walkable:
            self.index_x += 1
        elif trigger[self.place_bomb] and can_place:
            return self.bomb_handler()
        else:
            return None
