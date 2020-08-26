import socket
s=socket.socket()
host="192.168.56.1"
port=30000
s.bind((host, port))
s.listen()
print("Waiting for two connection...")

#si connette il primo
conn1, address1=s.accept()
print("Client one has connected")
conn1.send("Welcome to the server, client one!".encode())

#si connette il secondo
conn2, address2=s.accept()
print("Client two has connected")
conn2.send("Welcome to the server client two!".encode())

while True:
    #manda un messaggio
    msg=str(input(">>> "))
    msg=msg.encode()
    conn1.send(msg)
    conn2.send(msg)
    
    #riceve il messaggio da 1
    msg=conn1.recv(4096)
    msg=msg.decode()
    print("Client One:", msg)
    #e lo passa a due
    msg="Client One: "+msg
    conn2.send(msg.encode())
    
    #riceve il messaggio da 2
    msg=conn2.recv(4096)
    msg=msg.decode()
    print("Client Two:", msg)
    conn1.send(msg.encode())
    
    msg="Client Two: "+msg
    conn1.send(msg.encode())