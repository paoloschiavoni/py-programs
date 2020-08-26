from cardsPerBlack import Card
from deckPerBlack import Deck
import random

class Player(object):#crea il giocatore

    def __init__(self, cards):
        self.cards=cards

    def __str__(self):
        result=""
        result= ", ".join(map(str, self.cards))+"\n"+ str(self.getPoints())+" punti \n"
        return result

    def hit(self, deck):
        self.cards.append(deck.getCard())

    def getPoints(self):
        result=0
        for card in self.cards:
            card=list(card)
            if card[0] in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                result+=int(card[0])
            elif card[0] in [10, 11, 12, 13]:
                result+=10
            for card in self.cards:
                card=list(card)
                if card[0]==1:
                    if result > 21:
                        result-=10
            
        return result


class Dealer(Player):#crea il dealer

    def __init__(self, card):
        Player.__init__(self, card)
        self.showOneCard=True
        
    def __str__(self):
        if self.showOneCard:
            result=""
            result=str(self.cards[0])+"\n"+str(self.getPoints())+" punti \n"
            return result
        else:
            return str(self.cards)

    def hit(self, deck):#somma le carte se il punteggio è minore di 17 e fa visualizzare tutto
        self.showOneCard=False
        while self.getPoints() <17:
            self.cards.append(deck.getCard())


class Blackjack(object):
    
    def __init__(self):
        self.deck=Deck()
        self.deck.shuffle()

        #da le carte al giocatore e al dealer
        self.player=Player([self.deck.getCard(), self.deck.getCard()])
        self.dealer=Dealer([self.deck.getCard(), self.deck.getCard()])

    def play(self):

        print("Player:\n", self.player)
        print("Dealer:\n", self.dealer)

        while True:
            choice=str(input("Un'altra? [s/n]: "))
            if choice == "s":
                self.player.hit(self.deck)
                points=self.player.getPoints()
                print("Player:\n", self.player)
            else:
                break

        playerPoints=self.player.getPoints()
        if playerPoints > 21:
            print("Hai sballato, fai schifo")
        else:
            #turno del dealer
            self.dealer.hit(self.deck)
            print("Dealer: \n", self.dealer, "\n", self.dealer.getPoints(), " punti \n")

        dealerPoints=self.dealer.getPoints()

        if dealerPoints>21:
            print("Il dealer ha sballato, hai vinto!")
        elif dealerPoints==playerPoints:
            print("Pareggio incredibbbile!")
        elif dealerPoints>playerPoints:
            print("Vince il dealer, fai schifo!")
        elif dealerPoints<playerPoints:
            print("Hai vinto, rip dealer")
