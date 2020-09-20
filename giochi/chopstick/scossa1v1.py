from tkinter import *

class Scossa(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title('scossa 1v1')
        self.grid()
        
        self.p1=[1, 1]
        self.p2=[1, 1]
        self.turnogiocatore=1
        
        self.drawstatus()
        #write the numbers
        self.numbers=StringVar()#i numeri per attaccare o per splittare
        self.numentry=Entry(self, textvariable=self.numbers)
        self.numentry.grid(row=3, column=0)
        
        #attack and split buttons
        self.attackbutton=Button(self, text='attack', command=self.attack)
        self.attackbutton.grid(row=4, column=0)
        self.splitbutton=Button(self, text='split', comman=self.split)
        self.splitbutton.grid(row=4, column=1)
        self.restartbutton=Button(self, text='restart', command=self.restart)
        self.restartbutton.grid(row=2, column=3)
    
    def drawstatus(self):
        
        self.p1[0]=self.p1[0]%5
        self.p1[1]=self.p1[1]%5
        self.p2[0]=self.p2[0]%5
        self.p2[1]=self.p2[1]%5
        
        self.label1=Label(self, text=str(self.p1[0])+'          '+str(self.p1[1]))
        self.label1.grid(row=0, column=0)
        self.label2=Label(self, text=str(self.p2[0])+'          '+str(self.p2[1]))
        self.label2.grid(row=1, column=0)
        
        #turn
        self.turnlabel=Label(self, text='turno del giocatore '+str(self.turnogiocatore)+'\n')
        self.turnlabel.grid(row=2, column=0)
        
        
    def attack(self):
        self.attackvalues=self.numentry.get()
        self.attackvalues=self.attackvalues.split(' ')
        self.attackvalues=list(map(int, self.attackvalues))
        
        for el in self.attackvalues:
            if el==0:
                return False
                
        self.contatore_attacco=-1
        self.contatore_difesa=-1
        self.contatorestessoattacco=0#nel caso ci fossero stessi numeri
        
        if self.turnogiocatore%2==1:
            for attacco in self.p1:
                if self.contatorestessoattacco==0:
                    self.contatore_attacco+=1
                    if self.attackvalues[0]==attacco:
                        for difesa in self.p2:
                            if self.contatorestessoattacco==0:
                                self.contatore_difesa+=1
                                if self.attackvalues[1]==difesa:
                                    self.p2[self.contatore_difesa]+=self.p1[self.contatore_attacco]
                                    self.contatorestessoattacco+=1
                                    self.turnogiocatore+=1
                                    if self.vittoria1():
                                        self.turnlabel['text']='ha vinto il giocatore 1\n'
                                        self.accorgimentivittoria()
                                        return False
        else:
            for attacco in self.p2:
                if self.contatorestessoattacco==0:
                    self.contatore_attacco+=1
                    if self.attackvalues[0]==attacco:
                        for difesa in self.p1:
                            if self.contatorestessoattacco==0:
                                self.contatore_difesa+=1
                                if self.attackvalues[1]==difesa:
                                    self.p1[self.contatore_difesa]+=self.p2[self.contatore_attacco]
                                    self.contatorestessoattacco+=1
                                    self.turnogiocatore-=1
                                    if self.vittoria2():
                                        self.turnlabel['text']='ha vinto il giocatore 2\n'
                                        self.accorgimentivittoria()
                                        return False

        self.turnlabel['text']=''
        self.drawstatus()
        
    def split(self):
        self.attackvalues=self.numentry.get()
        self.attackvalues=self.attackvalues.split(' ')
        self.attackvalues=list(map(int, self.attackvalues))
        if (self.attackvalues[0]==0 and self.attackvalues[1]==5) or (self.attackvalues[0]==5 and self.attackvalues[1]==0):
            return False
        
        if self.turnogiocatore%2==1:
            if self.attackvalues[0]==self.p1[0] or self.attackvalues[0]==self.p1[1]:
                return False
            self.somma=self.p1[0]+self.p1[1]
            for i in range(0, self.somma+1):
                if (i==self.attackvalues[0] and self.somma-i==self.attackvalues[1]) or (i==self.attackvalues[1] and self.somma-i==self.attackvalues[0]):
                    self.p1=[self.attackvalues[0], self.attackvalues[1]]
                    self.turnogiocatore+=1
                    self.drawstatus()
                    return False
                    
        if self.turnogiocatore%2==0:
            if self.attackvalues[0]==self.p2[0] or self.attackvalues[0]==self.p2[1]:
                return False
            self.somma=self.p2[0]+self.p2[1]
            for i in range(0, self.somma+1):
                if (i==self.attackvalues[0] and self.somma-i==self.attackvalues[1]) or (i==self.attackvalues[1] and self.somma-i==self.attackvalues[0]):
                    self.p2=[self.attackvalues[0], self.attackvalues[1]]
                    self.turnogiocatore-=1
                    self.drawstatus()
                    return False
            
    
    def vittoria1(self):
        self.p1[0]=self.p1[0]%5
        self.p1[1]=self.p1[1]%5
        self.p2[0]=self.p2[0]%5
        self.p2[1]=self.p2[1]%5
        
        if self.p2==[0, 0]:
            return True
            
    def vittoria2(self):
        self.p1[0]=self.p1[0]%5
        self.p1[1]=self.p1[1]%5
        self.p2[0]=self.p2[0]%5
        self.p2[1]=self.p2[1]%5
        
        if self.p1==[0, 0]:
            return True
    
    def accorgimentivittoria(self):
        self.label1['text']=str(self.p1[0])+'          '+str(self.p1[1])
        self.label2['text']=str(self.p2[0])+'          '+str(self.p2[1])
        self.attackbutton['state']=DISABLED
        self.splitbutton['state']=DISABLED
    
    def restart(self):
        self.p1=[1, 1]
        self.p2=[1, 1]
        self.turnogiocatore=1
        
        self.drawstatus()
        self.attackbutton['state']=NORMAL
        self.splitbutton['state']=NORMAL
        

Scossa().mainloop()