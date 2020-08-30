#in the attack comp
import socket

s=socket.socket()
port=55555
host='192.168.56.1'

s.bind((host, port))
s.listen()
conn, address=s.accept()

while True:
    a=conn.recv(4096).decode()
    print(a)
    a=str(input('>>> '))
    conn.send(a.encode())