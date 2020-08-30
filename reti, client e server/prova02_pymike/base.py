#funzioni principali:
#s.gethostname() restituisce il nome dell'host che stai usando
#s.gethostbyname() da indirizzo ip associato al nome dell'host
#s.send() invia segnali al TCP
#s.recv() riceve "
#s.close() chiude il socket

#doppio ## se lho tolto anche se sarebbe programma

import socket
s=socket.socket()#creo il socket e uso le opzioni predefinite (AF_INET, SOCK_STREAM)
s.connect(("ww.google.it", 80))#mi connetto a google con tupla con sito e porta utilizzata

#richiesta get homepage google
richiesta= "GET / HTTP/1.1\nHost: www.google.it\n\n"
s.send(richiesta.encode()) #encode perchè la richiesta richiede l'oggetto in bytes

#ottengo la risposta alla richiesta
risposta=s.recv(2048)
#indica il buffersize, ovvero la quantità di dati da scaricare alla volta
#dato che magari la pagina potrebbe essere molto grande
##print(risposta)#da solo la prima parte, ma se voglio avere tutto:

##while len(risposta)>0:
##    print(risposta)
##   risposta=s.recv(2048)
##alla fine chiudere il socket
s.close()
print(s)

'''
passi da fare:

PER SOCKET CLIENT:
    -creazione socket                   socket.socket(AF_INET, SOCK_STREAM)
    -connessione al server              s.connect(indirizzo)                    -> indirizzo= pagina/id, porta utilizzata
    -invio richiesta al server          s.send(richiesta.encode())              -> richiesta= "GET / HTTP/1.1\n Host: indirizzo (es: www.google.it)
    -ricevere richiesta al server       s.recv(buffersize)                      -> buffersize= grandezza con cui scaricare man mano i file

PER SOCKET SERVER:
    -creare socket                                                              s.socket()
    -collegamento all'indirizzo della macchina e della porta designata          s.bind()
    -messa in ascolto in attesa della connessione del server                    s.listen()
    -accettazione del client                                                    s.accept()
    -ricezione richiesta del client                                             s.recv()
    -elaborazione risposta                                                      s.subprocess()
    -invio risposta al client                                                   s.send()
'''