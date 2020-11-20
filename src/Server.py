import socket
from _thread import *
import pickle

from Character import Character
import player_id
import pygame as pg
from Mlevel import Level

server = (socket.gethostbyname(socket.gethostname()))
port = 5555
l = Level(player_id.game_surface)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

characters = [Character(3, player_id.PLAYER_ONE_ID, 1, 1, player_id.game_surface, (255, 0, 0), pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_SPACE),
              Character(3, player_id.PLAYER_TWO_ID, 13, 1, player_id.game_surface, (0, 255, 0), pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_SPACE)]
levels = [Level(player_id.game_surface)]
# amount of clients to connect to the server
s.listen(4)
print("Server started on: ", server)
print("Waiting for connection")


def threaded_client(conn, character, level):
    # conn.send(pickle.dumps(characters[character]))
    # conn.send(pickle.dumps(levels[level]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            data2 = pickle.loads(conn.recv(2048))
            # characters[character] = data
            # levels[level] = data2
            if not data:
                print("Disconnected")
                break
            else:
                # if characters == 1:
                #     reply = characters[0]
                # else:
                #     reply = characters[1]

                print("Received: ", data)
                print("Sending : ", reply)

            if not data2:
                print("Disconnected")
                break
            else:
                # if levels == 1:
                #     reply = levels[0]
                print("Received: ", data2)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0
while True:
    conn, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
