import socket
import pickle
from _thread import start_new_thread
import pygame as pg
import const
from character import Character
from mlevel import Level


class Client:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (socket.gethostbyname(socket.gethostname()))
        self.port = 5555
        self.address = (self.server, self.port)
        self.characters = [Character(3, const.PLAYER_ONE_ID, 1, 1, const.surface, (255, 0, 0)),
                           Character(3, const.PLAYER_TWO_ID, 13, 1, const.surface, (0, 255, 0))]
        self.level = Level(const.surface)
        self.client_thread = start_new_thread(self.data_receiver, ())

    def data_receiver(self):
        self.socket.connect(self.address)
        while True:
            received = self.socket.recv(2048 * 8)
            client_id, ACTION, data = pickle.loads(received)
            self.update_gamestate(client_id, ACTION, data)

    def send(self, ACTION, data=None):
        pickled_data = pickle.dumps((ACTION, data))
        try:
            self.socket.send(pickled_data)
            print(f'sent from {self.socket.getsockname()}')
        except socket.error as e:
            print(e)
            print(data)

    def update_gamestate(self, client_id, ACTION, data):
        if ACTION == const.SERVER_UPDATE_POS:
            for c, updated_c in zip(self.characters, data):
                c.index_x = updated_c[0]
                c.index_y = updated_c[1]

        # if ACTION == const.SERVER_PLANT_BOMB:
        #     player_id = data[0]
        #     bomb_index = data[1]
        #     self.characters[player_id].bomb_handler()
