import socket
import time
from _thread import *
import pickle
from character import Character
import const
from mlevel import Level


class Server:
    def __init__(self):
        # initializing variables and lists
        self.multiplier = 8
        self.port = 5555
        self.addr = (socket.gethostbyname(socket.gethostname()))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.addr, self.port))
        self.socket.listen(2)
        self.clients = []
        self.characters = [Character(3, const.PLAYER_ONE_ID, 1, 1, None, (255, 0, 0)),
                           Character(3, const.PLAYER_TWO_ID, 13, 1, None, (0, 255, 0))]
        self.bombs = []
        self.ready_clients = 0
        self.level = Level(None)
        self.active = True
        self.connectThread = start_new_thread(self.make_connections, ())
        self.bombThread = start_new_thread(self.bomb_manager, ())

    # method to manage the bombs placement and when they are exploding
    def bomb_manager(self):
        while self.active:
            curr_time = time.time()
            if self.bombs:
                for b in self.bombs:
                    if b.is_exploding(curr_time):
                        self.characters[b.PLAYER_ID].bomb_count -= 1
                        b.bomb_explode(self.level.tile_array)
                        for c in self.characters:
                            if c.check_death(b):
                                self.respond_all(client_id=b.PLAYER_ID, ACTION=const.SERVER_KILL_PLAYER, data=c.PLAYER_ID)
                        self.respond_all(client_id=b.PLAYER_ID, ACTION=const.SERVER_DESTROY_TILES, data=b.list)
                        # if the tile is bombed and it is explodable, the tile will become walkable, and no longer visible
                        for index_x, index_y in b.list:
                            self.level.tile_array[index_x, index_y].visible = False
                            self.level.tile_array[index_x, index_y].walkable = True
                self.bombs = [b for b in self.bombs if b.is_live]

    # method that connects the players
    def make_connections(self):
        client_id = 0
        while len(self.clients) < 2:
            connection, addr = self.socket.accept()
            self.clients.append((connection, client_id))
            start_new_thread(self.receive_from_client, (client_id, connection))
            client_id += 1

    # method that receives from the client
    def receive_from_client(self, client_id, connection):
        while self.active:
            try:
                received = connection.recv(2048*8)
            except ConnectionAbortedError as e:
                print(e)
                continue
            except ConnectionResetError as e:
                print(e)
                continue
            curr_client_id, ACTION, data = pickle.loads(received)
            if curr_client_id is not None:
                self.update_gamestate(curr_client_id, ACTION)
            else:
                self.update_gamestate(client_id, ACTION)
    # method that updates the gamestates
    def update_gamestate(self, client_id, ACTION):
        if ACTION == const.CLIENT_CONNECT and self.ready_clients < 2:
            self.respond_one(client_id, const.SERVER_GIVE_ID, client_id)
            self.ready_clients += 1
        if self.ready_clients == 2:
            c_char = self.characters[client_id]
            if ACTION == const.CLIENT_QUIT:
                self.respond_all(client_id, const.SERVER_KILL_GAME)
                self.active = False
            elif ACTION == const.CLIENT_MOVE_DOWN:
                if c_char.index_y < 14 and self.level.tile_array[c_char.index_x, c_char.index_y + 1].walkable:
                    self.characters[client_id].index_y += 1
                    response = [(c.index_x, c.index_y) for c in self.characters]
                    self.respond_all(client_id, const.SERVER_UPDATE_POS, response)
            elif ACTION == const.CLIENT_MOVE_UP:
                if c_char.index_y > 0 and self.level.tile_array[c_char.index_x, c_char.index_y - 1].walkable:
                    self.characters[client_id].index_y -= 1
                    response = [(c.index_x, c.index_y) for c in self.characters]
                    self.respond_all(client_id, const.SERVER_UPDATE_POS, response)
            elif ACTION == const.CLIENT_MOVE_LEFT:
                if c_char.index_x > 0 and self.level.tile_array[c_char.index_x - 1, c_char.index_y].walkable:
                    self.characters[client_id].index_x -= 1
                    response = [(c.index_x, c.index_y) for c in self.characters]
                    self.respond_all(client_id, const.SERVER_UPDATE_POS, response)
            elif ACTION == const.CLIENT_MOVE_RIGHT:
                if c_char.index_x < 14 and self.level.tile_array[c_char.index_x + 1, c_char.index_y].walkable:
                    self.characters[client_id].index_x += 1
                    response = [(c.index_x, c.index_y) for c in self.characters]
                    self.respond_all(client_id, const.SERVER_UPDATE_POS, response)
            elif ACTION == const.CLIENT_PLANT_BOMB:
                bomb = c_char.bomb_handler()
                if bomb is not None:
                    can_place = True
                    for b in self.bombs:
                        if b.index_x == bomb.index_x and b.index_y == bomb.index_y:
                            can_place = False
                    if can_place:
                        c_char.bomb_count += 1
                        self.bombs.append(bomb)
                        self.respond_all(client_id, const.SERVER_PLANT_BOMB, bomb)
    # method that responds to all
    def respond_all(self, client_id, ACTION, data=None):
        dump = pickle.dumps((client_id, ACTION, data))
        for c, _ in self.clients:
            c.send(dump)
    # method that responds to one
    def respond_one(self, client_id, ACTION, data=None):
        dump = pickle.dumps((client_id, ACTION, data))
        self.clients[client_id][0].send(dump)
