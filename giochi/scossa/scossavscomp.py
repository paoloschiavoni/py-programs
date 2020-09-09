'''
gioco scossa contro il computer
'''
import random
import time

class Scossa_vs_comp(object):
    def __init__(self, status):
        self.computer=status[0]
        self.human=status[1]
        print('\nhuman:        ', self.human[0], '   ', self.human[1], '\n\ncomputer:     ', self.computer[0], '   ', self.computer[1])
        self.turno_human()
        
    def turno_human(self):
        self.attack_or_split=str(input('\nattack or split? [a/s]\n>>> '))
        
        if self.attack_or_split=='a':
            self.attack()
        if self.attack_or_split=='s':
            self.split()
        if self.attack_or_split!='a' and self.attack_or_split!='s' and self.attack_or_split!='quit':
            self.turno_human()
        
    def attack(self):
        self.giocata=input('\nattack move?\n>>> ')
        self.giocata=self.giocata.split(' ')
        self.giocata=list(map(int, self.giocata))
        
        self.contatore_attacco=-1
        self.contatore_difesa=-1
        
        for attacco in self.human:
            if attacco!=0:
                self.contatore_attacco+=1
                for difesa in self.computer:
                    if difesa!=0:
                        self.contatore_difesa+=1
                        if attacco==self.giocata[0] and difesa==self.giocata[1]:
                            print(self.contatore_attacco, self.contatore_difesa)
                            self.computer[self.contatore_difesa%2]=(self.computer[self.contatore_difesa%2]+self.human[self.contatore_attacco])%5
                            print('\nhuman:        ', self.human[0], '   ', self.human[1], '\n\ncomputer:     ', \
                            self.computer[0], '   ', self.computer[1])
                            self.vittoria()
                            self.turno_computer()
        else:
            self.attack()
    
    def split(self):
        
        self.contatore_split=-1
        
        self.giocata=input('\nsplit move?\n>>> ')
        self.giocata=self.giocata.split(' ')
        self.giocata=list(map(int, self.giocata))
        
        for i in self.giocata:
            for j in self.human:
                if i==j:
                    self.split()
        
        self.somma=self.human[0]+self.human[1]
        
        for i in range(self.somma+1):
            self.contatore_split+=1
            if (i==self.giocata[0] and (self.somma-i)==self.giocata[1]) or (i==self.giocata[1] and (self.somma-i)==self.giocata[0]):
                self.human=[self.giocata[0], self.giocata[1]]
                print('\nhuman:        ', self.human[0], '   ', self.human[1], '\n\ncomputer:     ', self.computer[0], '   ', self.computer[1])
                self.vittoria()
                self.turno_computer()
            if self.contatore_split==self.somma:
                self.split()
                
        
        
    def turno_computer(self):
        print('\ngiocata computer: \n')
        time.sleep(2)

        #final atk
        for i in range(1, 6):
            if self.human==[0, i] or self.human==[i, 0]:
                for j in self.computer:
                    if j+i==5:
                        self.human=[0, 0]
                        self.fine_turno_comp()
        
        #split nel caso avesse una mano sola
        for i in range(2, 5):
            if self.computer==[0, i] or self.computer==[i, 0]:
                self.somma=self.computer[0]+self.computer[1]
                if self.computer==[0, 4] or self.computer==[4, 0]:
                    self.computer=[2, 2]
                    self.fine_turno_comp()
                else:
                    self.computer=[1, self.somma-1]
                    self.fine_turno_comp()

        #solo un 1
        if self.computer==[0, 1] or self.computer==[1, 0]:
            i=random.choice([0, 1])
            if self.human[i]!=0:
                self.human[i]=(self.human[i]+1)%5
                self.fine_turno_comp()
            if self.human[i]==0:
                self.human[(i+1)%2]=(self.human[(i+1)%2]+1)%5
                self.fine_turno_comp()


        #attaco casuale nel caso tutti avessero due mani
        else:
            i=random.choice([0, 1])
            j=random.choice([0, 1])
            self.human[i]=(self.human[i]+self.computer[j])%5
            self.fine_turno_comp()

            

    def fine_turno_comp(self):

        print('\nhuman:        ', self.human[0], '   ', self.human[1], '\n\ncomputer:     ', self.computer[0], '   ', self.computer[1])
        
        self.vittoria()
        self.turno_human()

    def vittoria(self):
        if self.human==[0, 0]:
            print('\nvince il computer\n')
            exit()
        if self.computer==[0, 0]:
            print('\nhai vinto\n')
            exit()      

Scossa_vs_comp([[1, 3], [1, 3]])#il primo sarebbe il computer