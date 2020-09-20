somma=0
nvolte=0
while True:
    num=str(input("digita un numero, \npremi invio per visulaizzare la somma totale e la loro media: "))
    if num=="":
        break
    else:
        somma+=float(num)
        nvolte+=1
print("La somma è: ", somma,",", "La media è: ", somma/nvolte)
