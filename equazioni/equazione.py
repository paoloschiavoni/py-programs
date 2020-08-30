    #Risolve un'equazione di primo grado nell'incognita x
while True:
    equazione=str(input("Digita l'equazione\n\
    Usa lo spazio per dividere i vari elementi prima del segno\n\
    Non usare lo spazio per dividere l'uguale dagli elementi vicini\n>>>  "))

    listaDueMembri=equazione.split("=")

    contatore=0
    listaMembri1=[]
    listaMembri2=[]

    for membro in listaDueMembri:
        if contatore==0:
            listaMembri1=membro.split(" ")
        if contatore==1:
            listaMembri2=membro.split(" ")
        contatore+=1

    #Ora abbiamo le liste degli elementi nel primo membro e nel secondo
    #Con numero si intende sia gli elementi con l'incognite che quelli senza


    ####################################################
    ####################################################
    ################    TERMINI NOTI    ################
    ####################################################
    ####################################################


    listaIncognite1=[]
    listaNoti1=[]

    for numero in listaMembri1:
        if "x" in numero:
            listaIncognite1.append(numero)
        else:
            listaNoti1.append(numero)



    listaIncognite2=[]
    listaNoti2=[]

    for numero in listaMembri2:
        if "x" in numero:
            listaIncognite2.append(numero)
        else:
            listaNoti2.append(numero)


    #Adesso uniamo i termini noti dei due membri, cambiandogli di segno
    listaNoti=[]
    for termine in listaNoti1:
        listaNoti.append(int(termine))
    for termine in listaNoti2:
        termine= int(termine)*-1
        listaNoti.append(int(termine))

    #Calcoliamo la somma di tutti i termini noti e gli cambiamo di segno perchè li porto a secondo membro
    sommaNoti=0
    for termine in listaNoti:
        sommaNoti += termine
    sommaNoti=sommaNoti*-1


    ####################################################
    ####################################################
    ################     INCOGNITE     #################
    ####################################################
    ####################################################

    #Calcoliamo la somma tra i coefficienti del primo membro
    listaCoefficienti1=[]
    for incognita in listaIncognite1:
            listaDellIncognita=[]
            for el in incognita:
                if el != "x":
                    listaDellIncognita.append(el)
                    newEl=""
                    newEl="".join(listaDellIncognita)
            listaCoefficienti1.append(newEl)

    sommaCoefficienti1=0
    for el in listaCoefficienti1:
        sommaCoefficienti1+=int(el)

    #Ora qualla dei coefficienti del secondo
    listaCoefficienti2=[]
    for incognita in listaIncognite2:
            listaDellIncognita=[]
            for el in incognita:
                if el != "x":
                    listaDellIncognita.append(el)
                    newEl=""
                    newEl="".join(listaDellIncognita)
            listaCoefficienti2.append(newEl)

    sommaCoefficienti2=0
    for el in listaCoefficienti2:
        sommaCoefficienti2+=int(el)
    sommaCoefficienti2=sommaCoefficienti2*-1

    #Calcoliamo al somma dei coefficienti finali
    sommaCoefficientiFinali=sommaCoefficienti1+sommaCoefficienti2

    #Ecco la soluzione:
    print("\n>>>  x =", sommaNoti/sommaCoefficientiFinali)
    domanda=int(input("Vuoi continuare? 1: Sì   2: No"))
    if domanda==2:
        break
