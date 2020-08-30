### Il giocatore vince 4$ se nella coppia di dadi viene 7, altrimenti oer 1$. L'untente digita il numero di dollari e il programma restituisce il numero di tutni e i soldi vinti
###
import random
soldi= int(input("Digita il numero di soldi da giocare: "))
contatoreturni=0
winorlose=""
contatorevittorie=0
contatoresconfitte=0
qmax=soldi
print("%10s%10s%15s%15s%25s" % ("Turno", "1°dado", "2°dado", "win or lose", "Soldi"))
while True:
    contatoreturni +=1
    numdado1= random.randint(1, 7)
    numdado2= random.randint(1, 7)

    if numdado1+numdado2==7:
        soldi += 4
        winorlose="win"
        contatorevittorie+=1

    if numdado1 + numdado2 != 7:
        soldi -= 1
        winorlose="lose"
        contatoresconfitte +=1

    if qmax <soldi:
        qmax=soldi
    print("%10s%10s%15s%15s%25s" % (contatoreturni, numdado1, numdado2, winorlose, soldi))
    if soldi == 0:
        break

print("Hai fatto: ", contatorevittorie, "vittorie e ", contatoresconfitte, "sconfitte")
print("La quantità massima di denaro raggiunto nel piatto è stata: ", qmax, "$")
