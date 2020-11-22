import socket
import pickle
import time
from _thread import start_new_thread
import const
from character import Character
from mlevel import Level
import pygame as pg


class Client:
    def __init__(self, surface):
        # initializing variables and lists
        self.alive_player = 2
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (socket.gethostbyname(socket.gethostname()))
        self.port = 5555
        self.surface = surface
        self.address = (self.server, self.port)
        self.characters = [Character(3, const.PLAYER_ONE_ID, 1, 1, const.surface, (255, 0, 0)),
                           Character(3, const.PLAYER_TWO_ID, 13, 1, const.surface, (0, 255, 0))]
        self.level = Level(const.surface)
        self.bombs = []
        self.client_thread = start_new_thread(self.data_receiver, ())
        self.client_id = None
        self.game_active = True
    # method that receives data
    def data_receiver(self):
        self.socket.connect(self.address)
        while True:
            received = self.socket.recv(2048 * 8)
            client_id, ACTION, data = pickle.loads(received)
            self.update_gamestate(client_id, ACTION, data)
    # methods that sends data to server
    def send(self, ACTION, data=None):
        pickled_data = pickle.dumps((self.client_id, ACTION, data))
        try:
            self.socket.send(pickled_data)
        except socket.error as e:
            print(e)
            print(data)
    # method that updates the gamestate
    def update_gamestate(self, client_id, ACTION, data):
        if ACTION == const.SERVER_GIVE_ID:
            self.client_id = data
        elif ACTION == const.SERVER_KILL_GAME:
            self.game_active = False
        elif ACTION == const.SERVER_KILL_PLAYER:
            self.characters[data].alive = False
            # shuts down both games
            self.game_active = False
        elif ACTION == const.SERVER_UPDATE_POS:
            for c, updated_c in zip(self.characters, data):
                c.index_x = updated_c[0]
                c.index_y = updated_c[1]
        elif ACTION == const.SERVER_PLANT_BOMB:
            data.plant_time = time.time()
            data.screen = self.surface
            self.bombs.append(data)
        elif ACTION == const.SERVER_DESTROY_TILES:
            explosion_list = data
            for index_x, index_y in explosion_list:
                pg.draw.circle(self.surface, self.characters[client_id].player_color,
                               (index_x * 32 + 217 + 16, index_y * 32 + 117 + 16), 16, 0)
                self.level.tile_array[index_x, index_y].visible = False
                self.level.tile_array[index_x, index_y].walkable = True