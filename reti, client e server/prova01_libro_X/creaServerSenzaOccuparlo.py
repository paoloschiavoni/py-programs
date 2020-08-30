from codecs import decode
from socket import *
from threading import Thread
from time import ctime

HOST="localhost"
PORT=33330
DIMENSIONEMAX=1024
ADDRESS=(HOST, PORT)
server=socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
print("ciao")
