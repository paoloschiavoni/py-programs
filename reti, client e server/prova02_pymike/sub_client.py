import socket
import sys

def conn_sub_server(indirizzo_server):
    try:
        s=socket.socket()
        s.connect(indirizzo_server)
        print(f"Connessione al server: {indirizzo_server} stabilita")
    except socket.error as errore:
        print(f"Qualcosa è andato storto, sto uscendo... \n{errore}")
        sys.exit()
    invia_comandi(s)

def invia_comandi(s):
    while True:
        comando=input(">>> ")
        if comando=="esc":
            print("sto chiudendo la connesione")
            s.close()
            sys.exit()
        else:
            s.send(comando.encode())
            data=s.recv(4096)
            print(data, "utf-8")

if __name__=="__main__":
    conn_sub_server(("192.168.56.1", 15098))