import socket
from _thread import *
import pickle

from character import Character
import const
import pygame as pg
from mlevel import Level

class Server:
    def __init__(self):
        self.port = 5555
        self.addr = (socket.gethostbyname(socket.gethostname()))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.addr, self.port))
        self.socket.listen(2)
        self.clients = []
        self.characters = [Character(3, const.PLAYER_ONE_ID, 1, 1, None, (255, 0, 0)),
                           Character(3, const.PLAYER_TWO_ID, 13, 1, None, (0, 255, 0))]
        self.level = Level(None)
        self.active = True
        self.connectThread = start_new_thread(self.threaded_client,())

    def threaded_client(self):
        while self.active:
            clientid = 0
            connection, addr = self.socket.accept()
            self.clients.append((connection, clientid))
            start_new_thread(self.receive_from_client, (clientid, connection, addr))
            clientid += 1


    def receive_from_client(self, client_id, connection, addr):
        while self.active:
            try:
                received = connection.recv(2048*8)
            except ConnectionAbortedError as e:
                print(e)
                continue
            except ConnectionResetError as e:
                print(e)
                continue
            ACTION, data = pickle.loads(received)
            self.update_gamestate(client_id, ACTION)

    def respond(self, clientid, ACTION, data):
        dump = pickle.dumps((clientid, ACTION, data))
        for c, _ in self.clients:
            c.send(dump)

    def update_gamestate(self, client_id, ACTION):
        print(f"updating gamestate for {client_id}")
        c_char = self.characters[client_id]
        if ACTION == const.CLIENT_MOVE_DOWN:
            print("move down requested")
            if c_char.index_y < 14 and self.level.tile_array[c_char.index_x, c_char.index_y + 1].walkable:
                print("move down granted")

                self.characters[client_id].index_y += 1
                response = [(c.index_x, c.index_y) for c in self.characters]
                self.respond(client_id, const.SERVER_UPDATE_POS, response)
        elif ACTION == const.CLIENT_MOVE_UP:
            if c_char.index_y > 0 and self.level.tile_array[c_char.index_x, c_char.index_y - 1].walkable:
                self.characters[client_id].index_y -= 1
                response = [(c.index_x, c.index_y) for c in self.characters]
                self.respond(client_id, const.SERVER_UPDATE_POS, response)
        elif ACTION == const.CLIENT_MOVE_LEFT:
            if c_char.index_x > 0 and self.level.tile_array[c_char.index_x - 1, c_char.index_y].walkable:
                self.characters[client_id].index_x -= 1
                response = [(c.index_x, c.index_y) for c in self.characters]
                self.respond(client_id, const.SERVER_UPDATE_POS, response)
        elif ACTION == const.CLIENT_MOVE_RIGHT:
            if c_char.index_x < 14 and self.level.tile_array[c_char.index_x + 1, c_char.index_y].walkable:
                self.characters[client_id].index_x += 1
                response = [(c.index_x, c.index_y) for c in self.characters]
                self.respond(client_id, const.SERVER_UPDATE_POS, response)
        # elif ACTION == const.CLIENT_PLANT_BOMB:
        #     pass


