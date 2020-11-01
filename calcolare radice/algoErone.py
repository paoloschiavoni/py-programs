class Erone():

    def __init__(self):#definisco tutte le variabili necessarie
        self.a=int(input('a: '))#numero di cui voglio trovare la radice
        self.x=self.a
        self.y=self.a/self.x
        self.contatore=0#il contatore serve per sapere a che passaggio siamo
        self.xprov=self.x#queste due variabili provvisorie servono a stoppare il programma nel caso si trovasse la radice:
        self.yprov=self.y#se la nuova x è uguale alla precedente, significa che la radice è stata trovata
        self.printradice()#da inizio alla funzione che printa le informazioni iniziali

    def printradice(self):
        print(self.contatore)
        print('x= '+str(self.x))
        print('y= '+str(self.y)+'\n')
        self.xprov=self.x#aggiorno le variabili provvisorie
        self.yprov=self.y
        self.trovaradice()#chiamo la funzione che calcola la nuova x e y

    def trovaradice(self):
        try:
            self.contatore+=1#aggiorno il contatore
            self.x=0.5*(self.x+(self.a/self.x))#calcolo la nuova x con l'argoritmo di erone
            self.y=self.a/self.x#nuova y
            if self.x==self.xprov:#nel caso la nuova x sia uguale alla precedente, il programma si stoppa,
                print('radice trovata\n\n')
                Erone()#chiamando la funzione che ne da la fine
            return self.printradice()#richiamo la funzione che printa il tutto
        except:#questo si attiva nel caso ci fosse un'errore, ovvero il numero massimo di passaggi raggiunto
            Erone()

Erone()
