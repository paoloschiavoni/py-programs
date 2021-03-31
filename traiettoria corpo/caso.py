f=open("dati.txt")
f=f.read()
dati=f.split("\n")
for count in range(9):
    dati.pop(-1)
print(dati.index('50'))
