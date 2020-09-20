import socket

class Network:
    def __init__(self):
        self.client=socket.socket()
        self.host='172.17.201.177'
        self.port=5555
        self.addr=(self.host, self.port)
        self.pos=self.connect()
    
    def getPos(self):
        return self.pos
    
    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(4096)
    
    def send_data(self, data):
        data=data.encode()
        self.client.send(data)
        return self.client.recv(4096).decode()