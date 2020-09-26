import socket
import keyboard
import time

s=socket.socket()
host=socket.gethostbyname(socket.gethostname())
port=5555
s.connect((host, port))
print('connesso')

left=0
right=0

while 1:

    if keyboard.is_pressed('left'):
        left+=1
        s.send('l'+str(left).encode())
    if keyboard.is_pressed('right'):
        right+=1
        s.send('r'+str(right).encode())
    
    else:
        msg=s.recv(20).decode()
        msg=list(msg)
        if msg[0]=='l':
            msg.remove('l')
            left=int(''.join(msg))
        if msg[0]=='r':
            msg.remove('r')
            right=int(''.join(msg))

    print(left, right)