from tkinter import *
from cards import Card
from deck import Deck

class CardDemo(Frame):

    def __init__(self, rank, seme):
        self.rank=rank
        self.seme=seme
        Frame.__init__(self)

        self.master.title("Carta")

        self.grid()
        self.deck=Deck()

        self.cardLabel=Label(self, text="Retro della carta")

        self.cardLabel.grid(row=0, column=0)

        self.newCardButton=Button(self, text="nuova carta", command=self.newCard)
        self.mischiaButton=Button(self, text="mischia", command=self.mischia)
        self.newDeckButton=Button(self, text="nuovo Deck", command=self.nuovoDeck)
        self.newCardButton.grid(row=0, column=1)
        self.mischiaButton.grid(row=1, column=1)
        self.newDeckButton.grid(row=2, column=1)

    def newCard(self):
        if len(self.deck) != 0:
            self.card=self.deck.getCard()
            self.cardLabel=Label(self, text="       "+str(self.card)+ "        ")
            self.cardLabel.grid(row=0, column=0)
        else:
            self.nuovoDeck()

    def mischia(self):
        self.deck.shuffle()

    def nuovoDeck(self):
        self.deck=Deck()
        self.cardLabel=Label(self, text="retro della carta")

def main():
    CardDemo(0, "").mainloop()

main()
