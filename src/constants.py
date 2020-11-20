import pygame as pg

# variables that are used to discern the different players
PLAYER_ONE_ID = 1
PLAYER_TWO_ID = 2

# Create surface from dimensions
width, height = 900, 700
surface = pg.display.set_mode((width, height))
game_surface = pg.display.set_mode((width, height))
