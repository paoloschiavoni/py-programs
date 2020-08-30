#   Modificare un'immagine
#1. Resize image
#2. Nitidezza
#3. Luminosità
#4. Contrasto
#5. Colori
#6. Sfocatura

from PIL import Image, ImageEnhance, ImageFilter
import os
contatore=0 #Se si volesse salvare l'immagine, il contatore serve per numerare la immagini salvate

def main(contatore):
    path=str(input("\nDigita il percorso dell'immagine sul pc\nSe gli 'slesh' sono così (\), sostituiscili con /\n>>>  "))
    os.chdir(path)
    pathImmagine=str(input("\nDigita il nome dell'immagine, aggiungendo il tipo di formato, con alla fine: .'tipo di formato'\n>>>  "))
    image=Image.open(pathImmagine)
    while True:
        contatore+=1
        comando=int(input("\nDigita il numero corrispondente al comando desiderato: \n1. Grandezza immagine\n2. Nitidezza\n3. Luminosità\n4. Contrasto\n5. Colori\n6. Sfocatura\n7. Bianco e Nero\n8. Quit\n>>>  "))
        if comando == 1:
             print(resize(image))
        if comando==2:
            print(nitidezza(image))
        if comando==3:
            print(luminosita(image))
        if comando==4:
            print(contrasto(image))
        if comando==5:
            print(cambiaColore(image))
        if comando==6:
            print(sfocatura(image))
        if comando ==7:
            print(biancoNero(image))
        if comando== 8:
            break
        if comando != 1 and comando != 2 and comando != 3 and comando != 4 and comando != 5 and comando != 6 and comando != 7:
            print("Errore. Comando non trovato.")
        salvare=str(input("\nSe ti piace l'immagine, puoi salvarla digitando si\nAltrimenti premi 'Invio' per tornare al menù principale\n>>>  "))
        if salvare=="si":
            image.save("ImmagineModificata"+str(contatore)+".jpg")
            print("\nL'immagine è stata salvate come ImmagineModificata", str(contatore), ".jpg")

        contatoreCambiaImmagine=str(input("\nSe vuoi cambiare l'immagine da modificare, digita si\nAltrimenti digita 'Invio'\nSe vuoi modificare un'immagine appena salvata, dopo digita il suo nome come quello che è apparito sopra, togliendo gli spazi\n>>>  "))
        if contatoreCambiaImmagine=="si":
                main(contatore)

#1. Resize immagine
def resize(image):
    width, height = image.size
    nuoveDimensioni=int(input("Digita la nuova lunghezza(l'altezza si regolerà di conseguenza mantendendo) in pixel\n>>>  "))
    size=(nuoveDimensioni, nuoveDimensioni)
    image.thumbnail(size)
    image.show()
    

#2. Nitidezza
def nitidezza(image):
    enhancer = ImageEnhance.Sharpness(image)
    quantita=float(input("Digita di quanto aumentare la nitidezza(insieme dei valori di luminosità, contrasto, ecc..)\nDigita un numero naturale\nSe digiti 1, resterà normale, più aumenti più aumenta la nitidezza\n>>>  "))
    enhancer.enhance(quantita).show()
    salvare=str(input("Se ti piace l'immagine (o tornare al menù principale), puoi salvarla digitando si\nAltrimenti premi 'Invio' per tornare al menù principale\n>>>  "))
    
#3. Luminosità
def luminosita(image):
    width, height=image.size
    quantita=int(input("Digita di quanto quoi aumentare la luminosità\nIl valore può essere anche negativo\nSe il valore si avvicina a 255 o -255, è probabile che l'immagine sarà rispettivamente bianca oppure nera\n>>>   "))
    for x in range(width):
        for y in range(height):
            r, g, b=image.getpixel((x, y))
            image.putpixel((x, y), (r+quantita, g+quantita, b+quantita))
    image.show()

#4. Contrasto
def contrasto(image):
    contrasto=int(input("Digita il numero corrispondente al contrasto desiderato\n>>>  "))
    enhancer=ImageEnhance.Color(image)
    enhancer.enhance(contrasto).show()
    salvare=str(input("Se ti piace l'immagine, puoi salvarla digitando si\nAltrimenti premi 'Invio' per tornare al menù principale\n>>>  "))
    
#5. Colori
def cambiaColore(image):
    colore=int(input("Digita il numero corrispondente del colore da usare come filtro per l'immagine tra:\n1. Rosso\n2. Verde\n3. Blu\n>>>  "))
    coloritovalori={1:"Rosso", 2:"Verde", 3:"Blu"}
    lettera=coloritovalori.get(colore)
    print(lettera)
    width, height=image.size
    for x in range(width):
       for y in range(height):
            a, b, c = image.getpixel((x, y))
            if lettera == "Rosso":
                image.putpixel((x, y), (255, b, c))
            if lettera =="Verde":
                image.putpixel((x, y), (a, 255, c))
            if lettera=="Blu":
                image.putpixel((x, y), (a, b, 255))
    image.show()
    
#6. Sfocatura
def sfocatura(image):
    quantita=int(input("Digita di quanto vuoi sfocare l'immagine\n>>>  "))
    image.filter(ImageFilter.GaussianBlur(radius=quantita)).show()
    
#7 Bianco e Nero
def biancoNero(image):
    width, height=image.size
    for x in range(width):
        for y in range(height):
            r, g, b=image.getpixel((x, y))
            media=(r+g+b)//3
            image.putpixel((x, y), (media, media, media))
    image.show()
    
main(contatore)