while True:#fa ricominciare il programma una volta finito
    a=int(input('\n\na: '))#il numero di cui voglio trovare la radice
    x=a#la base del rettangolo
    y=1#l'altezzza
    xprov=x#la x del valore n-1
    contatore=0#per contare il numero di passaggi
    while True:#cilco infinito
        contatore+=1
        x=0.5*(x+(a/x))#algoritmo di Erone
        y=a/x
        if xprov==x:#la radice calcolata è uguale a quella precedente
            break#fine del ciclo infinito
        print(contatore)
        print('x:', x)
        print('y:', y)
        print(x*y)
        xprov=x#aggiornoi la x prov
