f=open("dati.txt")
f=f.read()
dati=f.split("\n")
print(dati)

dati.pop(-6)
print(dati)
