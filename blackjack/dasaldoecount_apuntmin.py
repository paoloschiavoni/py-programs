while True:
    try:
        print('\n')
        saldo=float(input("saldo: "))
        counter=int(input("counter: "))
        if counter<saldo:
            divisore=0
            for i in range(counter):
                divisore+=2**i

            puntatamax= saldo*(2**(counter-1))/divisore
            print('puntatamax:', puntatamax)

            puntatamin=puntatamax/(2**(counter-1))
            print('puntatamin:', puntatamin)

    except:
        pass
