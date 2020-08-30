from cardsPerBriscola import Card 
import random

class Deck(object):
    
    def __init__(self):
        self.cards=[]
        for seme in Card.SEMI:
            for rank in Card.RANKS:
                CARD=(seme, rank)
                self.cards.append(CARD)

    def __str__(self):
        result=""
        for card in self.cards:
            result += str(card)+"\n"
        return result

    def shuffle(self):
        random.shuffle(self.cards)

    def getCard(self):
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)

    def addCard(self, seme, rank):
        self.cards.append((seme, rank))

    def riordina(self):
        self.cards.sort()

    #non c'entra ma serve nel programma briscola 
    def chiVince(self, seme1, seme2, semeBriscola, valueCartaGiocata1, valueCartaGiocata2):
        if seme1==seme2:
            if valueCartaGiocata1 > valueCartaGiocata2:
                return True
            else:
                return False
        if seme1 != seme2:
            if seme1==semeBriscola:
                return True
            elif seme2==semeBriscola:
                return False
            else:
                return True

