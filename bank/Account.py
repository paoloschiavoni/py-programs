class SavingsAccount(object):

        TASSO=0.02
            
        def __init__(self, nome, pin, saldo=0.0):
            self.nome=nome
            self.pin=pin
            self.saldo=saldo
        def __str__(self):
            result=""
            result+= "Nome: " + self.nome + "\n"
            result+= "Pin: " + str(self.pin) + "\n"
            result+= "Saldo: " + str(self.saldo) + "\n"
            return result

        def versamento(self, importo):
            self.saldo += importo
            return self.saldo

        def prelievo(self, importo):
            if importo >= self.saldo:
                return "Saldo insufficiente"
            elif importo<0:
                return "L'importo deve essere >= 0"
            else:
                self.saldo-=importo
                return None

        def computeInterest(self):
                #calcola, versa e visualizza gli ineressi
                interest=SavingsAccount.TASSO*self.getSaldo()
                self.versamento(interest)
                return interest
        
        def getSaldo(self):
            return self.saldo
        def getPin(self):
            return self.pin
        def getNome(self):
            return self.nome

        
