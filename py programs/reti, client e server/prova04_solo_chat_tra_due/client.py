import socket
from tkinter import *

class Chat(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title="Chat"
        self.grid()
        self.status_label=Label(self, text="client - connesso")
        self.status_label.grid(row=0, column=0)
        self.string=StringVar()
        self.entry=Entry(self, textvariable=self.string)
        self.entry.grid(row=1, column=0)
        self.inv_button=Button(self, text="invia messaggio", command=self.invia_messaggio)
        self.inv_button.grid(row=1, column= 1)
        self.rcv_button=Button(self, text="ricevi messaggio", command=self.ricevi_messaggio)
        self.rcv_button.grid(row=1, column= 2)
        self.text_label_rcv=Label(self, text="")
        self.text_label_rcv.grid(row=2, column=0)
        self.text_label_inv=Label(self, text="")
        self.text_label_inv.grid(row=2, column=1)
        self.start_socket()
    
    def start_socket(self):
        self.s=socket.socket()
        self.host="192.168.56.1"
        self.port=40000
        self.s.connect((self.host, self.port))
    
    def invia_messaggio(self):
        self.msg_inv=self.string.get()
        self.msg_inv=self.msg_inv.encode()
        self.s.send(self.msg_inv)
        self.text_label_inv['text']+=('\n'+self.msg_inv.decode())
        self.text_label_rcv['text']+='\n'

    def ricevi_messaggio(self):
        self.msg_rcv=self.s.recv(4096)
        self.text_label_rcv['text']+=('\n'+self.msg_rcv.decode())
        self.text_label_inv['text']+='\n'
Chat().mainloop()