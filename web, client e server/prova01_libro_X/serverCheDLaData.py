from socket import *
from time import ctime
from codecs import decode
from time import ctime

PORT=33330
HOST="localhost"
ADDRESS=(HOST, PORT)

server=socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('waiting for connection...')
    HOST="localhost"
    
    PORT=33330
    DIMENSIONEMAX=1024
    ADDRESS=(HOST, PORT)
    server=socket(AF_INET, SOCK_STREAM)
    server.bind(ADDRESS)

    print("...connected from:", ADDRESS)
