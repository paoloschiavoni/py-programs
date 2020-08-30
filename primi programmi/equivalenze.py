dizio={"km":"1000", "hm":"100", "dam": "10", "m":"1", "dm":"0.1", "cm":"0.01", "mm":"0.001"}
num=float(input("digita il numero senza unità di misura: "))
unitàdimisurainiziale=str(input("digità l'unità di misura: "))
iniziale=float(dizio.get(unitàdimisurainiziale, None))
unitàdimisurafinale=str(input("Digita l'unità di misura in cui vuoi trasformare il numero: "))
finale=float(dizio.get(unitàdimisurafinale, None))
valore=iniziale/finale
numfinale=num*valore
print(numfinale, unitàdimisurafinale)
