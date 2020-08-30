import random
from die import Die
class Player(object):

    def __init__(self):
        self._die1=Die()
        self._die2=Die()


    def getNumOfRolls(self):
        return len(self._rolls)
    
    def play(self):
        self._die1.roll()
        self._die2.roll()
        (v1, v2)=(self._die1.getValue(), self._die2.getValue())
        initialSum= v1+v2
        print(" "+str((v1, v2))+" "+ str(v1+v2)+"\n")
        if initialSum in (2, 3, 12):
            return ("Hai persooo!")
        elif initialSum in (7, 11):
            return ("Hai vintooo!")
        else:
            while True:
                self._die1.roll()
                self._die2.roll()
                (v1, v2)=(self._die1.getValue(), self._die2.getValue())
                somma=v1+v2
                if somma==7:
                    return (" "+str((v1, v2))+" "+ str(v1+v2)+"\n"+"Hai persooo!")
                    break
                if somma==initialSum:
                    return (" "+str((v1, v2))+" "+ str(v1+v2)+"\n"+"Hai vintoo!")
                    break
        
def playOneGame():
    player=Player()
    print(player.play())
