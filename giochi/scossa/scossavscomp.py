'''
gioco scossa contro il computer
'''

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
            self.contatore_attacco+=1
            if attacco!=0:
                for difesa in self.computer:
                    self.contatore_difesa+=1
                    if difesa!=0:
                        if attacco==self.giocata[0] and difesa==self.giocata[1]:
                            self.computer[self.contatore_difesa]=(self.computer[self.contatore_difesa]+self.human[self.contatore_attacco])%5
                            print('\nhuman:        ', self.human[0], '   ', self.human[1], '\n\ncomputer:     ', \
                            self.computer[0], '   ', self.computer[1])
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
                self.turno_computer()
            if self.contatore_split==self.somma:
                self.split()
                
        
        
    def turno_computer(self):
        print('\ngiocata computer: \n')
        time.sleep(2)
                
        self.turno_human()
        
        
Scossa_vs_comp([[1, 1], [1, 1]])