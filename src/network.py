import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = (socket.gethostbyname(socket.gethostname()))
        self.port = 5555
        self.address = (self.server, self.port)
        self.p = self.connect()

        self.multiplier = 8

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2084 * self.multiplier))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048 * self.multiplier))
        except socket.error as e:
            print(e)
