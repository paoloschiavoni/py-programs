parola=input("Parola: ")
distanza=int(input("digita la distanza: "))
parolafinale=""
for lettera in parola:
    valoreletterafinale=ord(lettera)+distanza
    if valoreletterafinale > ord("z"):
        valoreletterafinale=ord("a")+(distanza-(ord("z")-ord(lettera)+1))
    letterafinale=chr(valoreletterafinale)
    parolafinale += letterafinale
print(parolafinale)
