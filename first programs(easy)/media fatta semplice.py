a=0
lista=[]
while True:
    try:
        num=float(input("Digita la misura: "))
        lista.append(num)
        a += 1
    except ValueError:
        break  
somma=0##########
for el in lista:
    somma += el
media= somma/a
print(media)
