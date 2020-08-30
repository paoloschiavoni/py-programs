frase=input("Digita la frase da decriptare: ")
contatoredistanza =0
while contatoredistanza <= 39:
    frasefinale=""
    contatoredistanza += 1
    for carattere in frase:
        newcarattere=chr(ord(carattere)-contatoredistanza)
        frasefinale += newcarattere
    print(frasefinale)
    
    
