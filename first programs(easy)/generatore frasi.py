###Programma che genera frasi.

import random
### definisce tutte le parole necessarie
articolisogg=["il ", "un "]
nomisogg=["pazzo ", "pupazzo ", "signorazzo ", "razzo ", "burlonazzo ", "cavalierazzo "]
verbi1=["colpito ", "adempito ", "scalpito ", "stupito ", "concepito "]
nomiogg=["uno col lazzo ", "un palazzo ", "un razzo ", "un arazzo ", "un tifoso del lazio ", "un mazzo ", "un ragazzo "]
cong=["mentre ", "perchè ", "poichè ", "e ", "che ", "nel momento che ", "anche se ", "dato che ", "visto che "]
verbi2=["acclamava ", "confutava ", "fumava ", "decimava ", "formava ", "mangiava ", "infiammava ", "odorava "]
         
numfrasi=int(input("digita il numero di poesie magnifiche: "))
contatorefrasi=0
###ciclo while
while True:
    stringatot=""
    sogg1=random.choice(nomisogg)
    verbo=random.choice(nomisogg)
    articolo=random.choice(articolisogg)
    verbo1=random.choice(verbi1)
    cogg1=random.choice(nomiogg)
    congiunzione=random.choice(cong)
    verbo2=random.choice(verbi2)
    cogg2=random.choice(nomiogg)

    
    stringatot = articolo+sogg1+"ha "+verbo1+cogg1+congiunzione+verbo2+cogg2
    
    print(stringatot)

    contatorefrasi +=1
    if contatorefrasi==numfrasi:
        break
         
