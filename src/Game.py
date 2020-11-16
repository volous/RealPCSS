import player_id
from Character import Character
from Mlevel import Level
import pygame as pg
import time


class Game_handler:

    def __init__(self, game_surface):
        # Initialize level and characters
        self.game_surface = game_surface
        self.level = Level(0, 0, 0, 0, self.game_surface)

        self.char1 = Character(3, player_id.PLAYER_ONE_ID, 1, 1, 249, 149, self.game_surface,
                               (255, 0, 0), pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_SPACE)

        self.char2 = Character(3, player_id.PLAYER_TWO_ID, 13, 1, 633, 149, self.game_surface,
                               (0, 255, 0), pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_k)

        self.characters = [self.char1, self.char2]

        self.bombs = []

    def draw(self):
        self.level.draw()
        self.actions()
        self.bomb_actions()

    def bomb_actions(self):
        for b in self.bombs:
            if not b.placed:
                b.bomb_explode(self.level.tile_array)
                chars = [c for c in self.characters if c.PLAYER_ID == b.PLAYER_ID]
                chars[0].bomb_count -= 1
                self.characters = [c for c in self.characters if not c.check_deth(b)]
                self.bombs.remove(b)
            else:
                b.draw_bomb(time.time())

    def actions(self):
        for c in self.characters:
            can_place = True
            for b in self.bombs:
                if b.index_x == c.index_x and b.index_y == c.index_y:
                    can_place = False
            bomb = c.player_actions(can_place, self.level.tile_array)
            if bomb is not None:
                self.bombs.append(bomb)
                c.bomb_count += 1
            c.draw()
