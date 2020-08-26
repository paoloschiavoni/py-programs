"""simula una banca con i vari account dal programma Account"""
from Account import SavingsAccount
class Bank(object):

    def __init__(self):
        self.accounts=[]

    def __str__(self):
        return "\n".join(map(str, self.accounts.values()))
    
    def add(self, account):
        """Aggiunge account alla banca"""
        self.accounts.append(account)
        
    def get(self, PIN):
        """Dato il pin restituisce l'account associato"""
        for account in self.accounts:
            name, pin, saldo=account
            if pin==PIN:
                return account

    def remove(self, pin):
        self.accounts.pop(pin, None)

    def computeInterest(self):
        #calcola gli interessi totali di tutti gli account
        tot=0.0
        for account in self.accounts:
            tot+=account.computeInterest()
        return tot

    def save(self, fileName=None):
        import pickle
        if fileName != None:
            self.fileName=fileName
        elif fileName == None:
            return
        fileObj=open(self.fileName, "wb")
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()
