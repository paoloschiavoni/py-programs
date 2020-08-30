from cardsPerBlack import Card 
import random

class Deck(object):
    
    def __init__(self):
        self.cards=[]
        for rank in Card.RANKS:
            for seme in Card.SEMI:
                CARD=[rank, seme]
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

    def addCard(self):
        rank=int(input("Rank della carta da aggiungere: "))
        seme=str(input("Seme della carta da aggiungere: "))
        newCard=(rank, seme)
        if newCard in self.cards:
            return "Carta già nel mazzo"
        else:
            self.cards.append(newCard)

    def riordina(self):
        self.cards.sort()

    def rimettiAPosto(self):
        for rank in Crad.RANKS:
            for seme in Card.SEMI:
                CARD=(rank, seme)
                if card not in self.cards:
                    self.cards.append(CARD)
        self.cards.sort()
