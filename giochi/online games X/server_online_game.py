import socket
from _thread import *
import sys

host='172.17.201.177'
port=5555

s=socket.socket()
s.bind((host, port))
s.listen(2)
print('waiting for connection...')

pos=[(0,0), (100,100)]

def read_pos(str):
    str=str.split(',')
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0])+','+str(tup[1])

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply=''

    while True:
        data=read_pos(conn.recv(4096).decode())
        pos[player]=data

        if not data:
            print('disconnected')
            break
        else:
            print('recived:', data)
            print('sending: ', reply)
            if player==1:
                reply=pos[0]
            else:
                reply=pos[1]
        conn.send(make_pos(reply).encode())

    print('connection lost')
    conn.close()

current_player=0

while True:
    conn, addr=s.accept()
    print('connected to', addr)
    print(current_player)
    start_new_thread(threaded_client, (conn, current_player))
    #creo un thread, in modo tale che mentre va questa funzione, intanto contunua a ricevere segnali
    current_player=1