from bank import Bank
from Account import SavingsAccount

class ATM(object):

    def __init__(self, bank):
        self.account=None
        self.bank=bank
        self.methods={}
        self.methods[1]=self.getSaldo
        self.methods[2]=self.prelievo
        self.methods[3]=self.versamento
        
    def run(self):
            name=str(input("Digita il nome: "))
            pin=input("Digita il tuo pin: ")
            saldo=int(input("Digita il saldo: "))
            account=name, saldo, pin
            self.bank.add(account)
            self.account=self.bank.getAccount(pin)
            if self.account==None:
                print("Errore: pin errato")
            else:
                self.runAccount()
            

    def runAccount(self):
        while True:
            print("1    Visulaizza saldo\n2    Prelievo\n3    Versamento\n")
            number=int(input("Digita un numero: "))
            method=self.methods[number]
            if number=="":
                break
            if method==None:
                print("Errore: comando inesistente")
            else:
                method()


    def getSaldo(self):
        name, saldo, pin=self.account
        print("Il saldo è: €"+ str(saldo))
        
    def prelievo(self):
        [name, saldo, pin]=self.account
        prelievo=int(input("Digita il prelievo: "))
        if prelievo>saldo:
            print("Saldo insufficiente")
        else:
            print("Ora il saldo è:", saldo-prelievo)
            self.account=list(self.account)
            self.account[1]=saldo-prelievo
        
    def versamento(self):
        name, saldo, pin=self.account
        versamento=int(input("Digita il versamento: "))
        print("Ora il saldo è:", saldo+versamento)
        self.account=list(self.account)
        self.account[1]=saldo+versamento

def main():
    bank=Bank()
    atm=ATM(bank)
    atm.run()
def createBank():
    number=int(input("Digita il numero di account: "))
    for i in range(number):
        nome=str(input("Digita il nome: "))
        saldo=int(input("Digita il saldo: "))
        pin=int(input("Digita il pin: "))
        bank.add(SaveAccount(nome+str(i), saldo, pin))


main()
