import socket
s=socket.socket()
host="192.168.56.1"
port=30000

s.connect((host, port))
print("Connected to the server")
msg=s.recv(4096).decode()
print("Server message: ", msg)

while True:
    #riceve messaggio
    msg=s.recv(4096)
    msg=msg.decode()
    print("Server: ", msg)
    
    #manda messaggio
    msg=str(input(">>> "))
    msg=msg.encode()
    s.send(msg)
    
    #riceve il messaggio di 2
    msg=s.recv(4096)
    msg=msg.decode()
    print(msg)