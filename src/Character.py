import pygame as pg
from Bomb import Bomb


class Character:
    def __init__(self, max_bombs, PLAYER_ID, index_x, index_y, posX, posY, screen, player_color, up, down, left, right,
                 place_bomb):
        self.bomb_count = 0
        self.max_bombs = max_bombs
        self.PLAYER_ID = PLAYER_ID
        self.index_x = index_x
        self.index_y = index_y
        self.posX = posX
        self.posY = posY
        self.width = 32
        self.height = 32
        self.vel = 32
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

    def draw(self):
        if self.alive:
            self.rect = pg.Rect((self.posX, self.posY, self.width, self.height))
            pg.draw.rect(self.screen, self.player_color, self.rect)

            font = pg.font.Font('freesansbold.ttf', 10)
            text = font.render(str((self.index_x, self.index_y)), True, (255, 255, 255), (0, 0, 0))
            self.screen.blit(text, (self.posX, self.posY))

    def check_deth(self, bomb):
        if (self.index_x, self.index_y) in bomb.list:
            self.alive = False
            return True
        return False

    def bomb_handler(self):
        if self.bomb_count < self.max_bombs:
            return Bomb(self.PLAYER_ID, self.explRad, self.posX, self.posY, True, True, self.screen,
                        self.index_x, self.index_y, self.player_color)

    def player_actions(self, can_place, tiles):
        trigger = pg.key.get_pressed()
        if trigger[self.up] and self.index_y > 0 and tiles[self.index_x, self.index_y - 1].walkable:
            self.posY -= self.vel
            self.index_y -= 1
        elif trigger[self.down] and self.index_y < 14 and tiles[self.index_x, self.index_y + 1].walkable:
            self.posY += self.vel
            self.index_y += 1
        elif trigger[self.left] and self.index_x > 0 and tiles[self.index_x - 1, self.index_y].walkable:
            self.posX -= self.vel
            self.index_x -= 1
        elif trigger[self.right] and self.index_x < 14 and tiles[self.index_x + 1, self.index_y].walkable:
            self.posX += self.vel
            self.index_x += 1
        elif trigger[self.place_bomb] and can_place:
            return self.bomb_handler()
        else:
            return None
