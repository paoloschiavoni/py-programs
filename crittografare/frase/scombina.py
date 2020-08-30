frase=input("frase: ")
distanza=int(input("digita la distanza(minore di 40: "))
frasefinale=""
for carattere in frase:
    carattere=chr(ord(carattere)+distanza)
    frasefinale+=carattere
print(frasefinale)

