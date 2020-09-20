#BRISCOLA A CARTE SCOPERTE PER DUE GIOCATORI

from deckPerBriscola import Deck
from cardsPerBriscola import Card

deck=Deck()

#Mischia il mazzo e pone la briscola
deck.shuffle()
briscola=deck.getCard()
print("La briscola è:", briscola, "\n\n")

(semeBriscola, rankBriscola)=briscola
briscola=Card(semeBriscola, rankBriscola)

deck.addCard(semeBriscola, rankBriscola)

#carte ai giocatori
cardsP1=[]
cardsP2=[]

while len(cardsP1) < 3:
    cardPescata=deck.getCard()
    cardsP1.append(cardPescata)
while len(cardsP2) < 3:
    cardPescata=deck.getCard()
    cardsP2.append(cardPescata)
    
resultP1=""
resultP2=""

for card in cardsP1:
    resultP1+= str(card)+"\n"
for card in cardsP2:
    resultP2+= str(card)+"\n"
    
print("Carte giocatore 1: \n"+resultP1+"\n\nCarte giocatore 2: \n", resultP2, "\n\nPer giocare una carta, digitate il numero della sua posizione\n\n")

#I mazzi delle carte vinte
mazzo1=[]
mazzo2=[]



#
#
#
#
#
#
#Inizio del gioco
#
#
#
#
#
#


while True:

    #I giocatori decidono di vedere le carte vinte digitando spazio,
    #altrimenti iniziano il turno
    
    vedereMazzo=str(input("Digitare spazio se si vogliono vedere i mazzi, con i rispettivi punteggi,\naltrimenti digitare invio"))
    print("\n")
    if vedereMazzo==" ":
        print("Carte vinte del giocatore 1:\n")
        for card in mazzo1:
            print(card, "\n")
        print("Carte vinte dal giocatore 2: \n")
        for card in mazzo2:
            print(card, "\n")

    #I giocatori digitano il numero della carta da giocare
    
    playP1=int(input("Giocatore 1 gioca una carta: "))
    playP2=int(input("Giocatore 2 gioca una carta: "))
    print("\n\n")

    cartaGiocata1=cardsP1.pop(playP1-1)
    cartaGiocata2=cardsP2.pop(playP2-1)
    

    #in base al valore della carta, che si ottiene da programma cardsPerBriscola,
    #si ottiene il vincitore del turno,
    #tenendo conto dei loro semi e di quello della briscola
    
    (seme1, rank1)=cartaGiocata1

    cartaGiocata1=Card(seme1, rank1)
    valueCartaGiocata1=cartaGiocata1.getValue()

    
    (seme2, rank2)=cartaGiocata2
    
    cartaGiocata2=Card(seme2, rank2)
    valueCartaGiocata2=cartaGiocata2.getValue()

    #Il giocatore che vince aggiunge le carte al suo mazzo
    #Poi pesca le carte per primo
    #Infine diventa il giocatore 1, che giocherà per primo al turno seguente
    
    if deck.chiVince(seme1, seme2, semeBriscola, valueCartaGiocata1, valueCartaGiocata2):#caso in cui il giocatore 1 vince
        print("Vince la carta del giocatore 1\n\n")
        continua=input("Digita invio per continuare")
        print("\n\n")
        mazzo1.append((seme1, rank1))
        mazzo1.append((seme2, rank2))

        if len(deck) != 0:
            cartaPescata1=deck.getCard()
            cartaPescata2=deck.getCard()

            cardsP1.append(cartaPescata1)
            cardsP2.append(cartaPescata2)

        if len(cardsP1)==0:
            break
        
        
        resultP1=""
        resultP2=""

        for card in cardsP1:
            resultP1+= str(card)+"\n"
        for card in cardsP2:
            resultP2+= str(card)+"\n"
            
        print("La briscola è:", (semeBriscola, rankBriscola), "\nCarte rimaste nel mazzo: ", len(deck), "\n\n")
        print("Carte giocatore 1: \n"+resultP1+"\n\nCarte giocatore 2: \n", resultP2, "\n\nPer giocare una carta, digitate il numero della sua posizione\n\n")

                
        #Caso in cui il giocatore 2 vince, ora i due giocatori si scambieranno,
        #dato che il secondo dovrà pescare per primo
        
    else:
        print("Vince la carta del giocatore 2\n\n")
        continua=input("Digita invio per continuare")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

        #scambia le carte del giocatore 2 con quelle del giocatore 1
        newCards1=[]
        newCards2=[]
        newCards1=cardsP1
        newCards2=cardsP2

        cardsP1=newCards2
        cardsP2=newCards1

        #scambia i mazzi del giocatore 2 con quelli del giocatore 1
        newMazzo1=[]
        newMazzo2=[]
        newMazzo1=mazzo1
        newMazzo2=mazzo2
        mazzo1=newMazzo2
        mazzo2=newMazzo1

        if len(deck) != 0:
            mazzo1.append((seme1, rank1))
            mazzo1.append((seme2, rank2))

            cartaPescata1=deck.getCard()
            cartaPescata2=deck.getCard()

            cardsP1.append(cartaPescata1)
            cardsP2.append(cartaPescata2)

        if len(cardsP1)==0:
            break
        
        resultP1=""
        resultP2=""

        for card in cardsP1:
            resultP1+= str(card)+"\n"
        for card in cardsP2:
            resultP2+= str(card)+"\n"

        
        print("Ora il giocatore 1 sarà il gicatore 2 e viceversa,\ndato che il giocatore 2 ha vinto\n\n")
        print("La briscola è:", (semeBriscola, rankBriscola), "\nCarte rimaste nel mazzo: ", len(deck), "\n\n")
        print("Carte giocatore 1: \n"+resultP1+"\n\nCarte giocatore 2: \n", resultP2, "\n\nPer giocare una carta, digitate il numero della sua posizione\n\n")

puntiP1=0
for card in mazzo1:
    (seme, rank)=card
    card=Card(seme, rank)
    valueCard=card.getValue()
    puntiP1+=valueCard
    
puntiP2=0
for card in mazzo2:
    (seme, rank)=card
    card=Card(seme, rank)
    valueCard=card.getValue()
    puntiP2+=valueCard

print("Punti giocatore 1: ", puntiP1)
print("Punti giocatore 2: ", puntiP2)
if puntiP1>puntiP2:
    print("Vince giocatore 1!")
elif puntiP1<puntiP2:
    print("Vince il giocatore numero 2!")
elif puntiP1==puntiP2:
    print("Pareggio!")
print("Gg")
