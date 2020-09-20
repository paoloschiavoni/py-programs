frase=input("frase: ")
distanza=int(input("digita la distanza: "))
frasefinale=""
for carattere in frase:
    carattere=chr(ord(carattere)+distanza)
    frasefinale+=carattere
print(frasefinale)

frasefinale2=""
for carattere in frasefinale:
    carattere=chr(ord(carattere)-distanza)
    frasefinale2 += carattere
print(frasefinale2)
