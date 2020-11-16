import socket
from _thread import *

server = (socket.gethostbyname(socket.gethostname()))
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

# amount of clients to connect to the server
s.listen(4)
print("Server started on: ", server)
print("Waiting for connection")


def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            # Amount of bits receiving
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            # If client don't send any data, he must be disconnected
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("sending: ", reply)

            conn.sendall(str.enconde(reply))
        except:
            break

    print ("Connection lost")
    conn.close()


while True:
    conn, address = s.accept()
    print("Connected to:", address)

    start_new_thread(threaded_client, (conn,))
