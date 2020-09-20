stato=[[1, 1], [1, 1]]
contatore=100

def swap(a, b):
    return [b, a]

def gioco(stato, contatore):
    risultato=-2
    
    if contatore==0:
        return 0
    
    if stato[1]==[0, 0]:
        return 1
    
    if stato[0]==[0, 0]:
        return -1
    
    contatore-=1
    
    for attacco in [0, 1]:
        if stato[0][attacco]==0:
            pass
        for difesa in [0, 1]:
            if stato[1][difesa]==0:
                pass
        
            newstato=stato
            newrisultato=risultato
            
            newstato[1][difesa]=(newstato[1][difesa]+stato[0][attacco])%5
            newstato=swap(newstato[0], newstato[1])
            newrisultato=gioco(newstato, contatore)*-1
            if newrisultato>risultato:
                risultato=newrisultato
                if risultato==1:
                    return risultato

    somma=stato[0][0]+stato[0][1]
    for count in range(somma):
    
        if count==stato[0][0] or count==stato[0][1] or count==0:
            pass
            
        newstato=stato
        newstato[0][0]=count%5
        newstato[0][1]=(somma-count)%5
        newstato=swap(newstato[0], newstato[1])
        newrisultato=gioco(newstato, contatore) * -1
        
        if newrisultato>risultato:
            risultato=newrisultato
            mossa=[count, somma - count]
            if risultato==1:
                return risultato
                    
    return risultato
    
print(gioco(stato, contatore))