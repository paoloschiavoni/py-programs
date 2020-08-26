import os, os.path

MENU="""

1    Elenca contenuti nella caretlla corrente
2    Vai su
3    Vai giù
4    Numero file nella cartella
5    Dimensione cartella in byte
6    Cerca un file
7    Esci

"""
COMANDI= ["1", "2", "3", "4", "5", "6", "7"]
QUIT= "7"

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command=acceptCommand()
        runCommand(command)
        if command==QUIT:
            print("Adios")
            break

def acceptCommand():
    """restituisce in input il numero e restituisce il comando"""
    while True:
        command=input("Digita il comando: ")
        if not command in COMANDI:
            print ("Errore: comando sconosciuto")
        else:
            return command

def runCommand(command):
    """Esegue il programma"""
    if command=="1":
        elencaContenuti(os.getcwd())
    elif command=="2":
        vaisu()
    elif command=="3":
        vaigiu()
    elif command =="4":
        print("Il numero dei file è: ", contaFile(os.getcwd()))
    elif command == "5":
        print("Il numero dei byte totali è: ", contaByte(os.getcwd()))
    elif command == "6":
        target = input("Digita la stringa da cercare: ")
        listaFile=trovaFile(target, os.getcwd())
        if not listaFile:
               print("Stringa non trovata")
        else:
            for el in listaFile:
                print(el)

def elencaContenuti(path):
    lista=os.listdir(path)
    for el in lista:
        print(el)

def vaisu():
        os.chdir("..")


def vaigiu():
        nuovaCartella=input("Digita il nome della nuova cartella: ")
        if os.path.exists(os.getcwd() + os.sep + nuovaCartella) and os.path.isdir(nuovaCartella):
               os.chdir(nuovaCartella)
        else:
               print("Cartella non trovata")

def contaFile(path):
    somma=0
    for el in os.listdir(os.getcwd()):
        if os.path.isfile(el):
            somma += 1
        else:
            os.chdir(el)
            somma += contaFile(os.getcwd())
            os.chdir("..")
    return somma


def contaByte(path):
    byte=0
    lista=os.listdir(os.getcwd())
    for el in lista:
        if os.path.isfile(el):
            byte += os.path.getsize(os.getcwd())
        else:
            os.chdir(el)
            byte += contaByte(os.getcwd())
            os.chdir("..")
    return byte


def trovaFile(target, path):
    files=[]
    lista=os.listdir(os.getcwd())
    for el in lista:
        if os.path.isfile(el):
            if target in el:
                files.append(path + os.sep + el)
        else:
            os.chdir(el)
            files.extend(trovaFile(target, os.getcwd()))
            os.chdir("..")
    return files

main()