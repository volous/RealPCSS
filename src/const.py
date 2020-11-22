import pygame as pg

# constants

PLAYER_ONE_ID = 0
PLAYER_TWO_ID = 1

# create surface from dimensions
width, height = 900, 700
surface = pg.display.set_mode((width, height))

# client actions
CLIENT_MOVE_LEFT = 10
CLIENT_MOVE_RIGHT = 11
CLIENT_MOVE_UP = 12
CLIENT_MOVE_DOWN = 13
CLIENT_PLANT_BOMB = 14
CLIENT_CONNECT = 15
CLIENT_QUIT = 16

# server actions
SERVER_UPDATE_POS = 20
SERVER_PLANT_BOMB = 21
SERVER_DESTROY_TILES = 22
SERVER_KILL_PLAYER = 23
SERVER_GIVE_ID = 24
SERVER_KILL_GAME = 25
