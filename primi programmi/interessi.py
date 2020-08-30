#input
saldoiniziale=float(input("digita l'importo iniziale: "))
numeroanni=int(input("digita il numero di anni: "))
tassoperc=float(input("Digita il tasso come percentuale: "))
#formato
print("%5s%18s%10s%18s" % ("Anno", "Saldo iniziale", "Interesse", "Saldo finale"))
b=0
a=0
for anno in range(1, numeroanni+1):
    interessi=saldoiniziale*tassoperc/100
    saldofinale=saldoiniziale+interessi
    print("%5s%16s%10s%16s" % (anno, round(saldoiniziale, 1), round(interessi, 1), round(saldofinale, 2)))
    saldoiniziale=saldofinale
    a=interessi
    b += a
print("Il guadagno totale è: ", b)
