from bank import Bank
from Account import SavingsAccount
from tkinter import *

class ATM(Frame):

    def __init__(self, bank):
        #creo la banca e un account=None
        Frame.__init__(self)
        self.master.title("ATM")
        self.grid()
        self.account=None
        self.bank=bank

        #crea tutte le etichette
        #nomi nella prima colonna
        self.nameLabel=Label(self, text="Name")
        self.PINLabel=Label(self, text="PIN")
        self.amountLabel=Label(self, text="Amount")
        self.statusLabel=Label(self, text="Status")

        self.nameLabel.grid(row=0, column=0)
        self.PINLabel.grid(row=1, column=0)
        self.amountLabel.grid(row=2, column=0)
        self.statusLabel.grid(row=3, column=0)

        #Var nella seconda colonna
        self.nameVar=StringVar()
        self.PINVar=StringVar()
        self.amountVar=DoubleVar()
        self.statusVar=StringVar()

        self.nameEntry=Entry(self, textvariable=self.nameVar, justify=CENTER)
        self.PINEntry=Entry(self, textvariable=self.PINVar, justify=CENTER)
        self.amountEntry=Entry(self, textvariable=self.amountVar, justify=CENTER)
        self.statusEntry=Entry(self, textvariable=self.statusVar, justify=CENTER)

        self.nameEntry.grid(row=0, column=1)
        self.PINEntry.grid(row=1, column=1)
        self.amountEntry.grid(row=2, column=1)
        self.statusEntry.grid(row=3, column=1)

        #Pulsanti dei comandi
        self.balanceButton=Button(self, text="Balance", command=self.balance)
        self.depositButton=Button(self, text="Deposit", command=self.deposit)
        self.withdrawButton=Button(self, text="Withdraw", comman=self.withdraw)
        self.loginButton=Button(self, text="Login", command=self.login)

        self.balanceButton.grid(row=0, column=2)
        self.depositButton.grid(row=1, column=2)
        self.withdrawButton.grid(row=2, column=2)
        self.loginButton.grid(row=3, column=2)

        self.balanceButton["state"]=DISABLED
        self.depositButton["state"]=DISABLED
        self.withdrawButton["state"]=DISABLED


    def balance(self):#da il saldo
        name, pin, saldo=self.account
        self.statusVar.set(("Hai €"+ str(saldo)))

    def deposit(self):#deposita
        amount=self.amountVar.get()
        self.account=list(self.account)
        self.account[2]+=amount
        self.statusVar.set("Deposit made")
        self.amountVar.set(0.0)

    def withdraw(self):#prelievo
        amount=self.amountVar.get()
        saldo=self.account[2]
        if saldo<amount:
            self.statusVar.set("Non hai abbastanza soldi")#messaggio di errore
        if amount<0:
            self.status.set("Amount deve essere >= 0")
        else:
            self.account[2]-=amount
            self.statusVar.set("withdrawal made")
        self.amountVar.set(0.0)

    def login(self):
        pin=self.PINVar.get()
        name=self.nameVar.get()
        self.account=self.bank.get(int(pin))#si ottiene l'account o None se non c'è
        if self.account != None:
            if self.account[0] == name:
                self.account=list(self.account)
                self.statusVar.set("Welcome")
                self.depositButton["state"]=NORMAL
                self.balanceButton["state"]=NORMAL
                self.withdrawButton["state"]=NORMAL
                self.loginButton["text"]="Logout"
                self.loginButton["command"]=self.logout
            if self.account[0] != name:
                self.statusVar.set("Name uncorrect")
        if self.account==None:
            self.statusVar.set("No PIN found")

    def logout(self):
        self.account=None
        self.nameVar.set("")
        self.PINVar.set("")
        self.statusVar.set("")
        self.amountVar.set(0.0)
        self.loginButton["command"]=self.login
        self.loginButton["text"]="Login"
        self.balanceButton["state"]=DISABLED
        self.depositButton["state"]=DISABLED
        self.withdrawButton["state"]=DISABLED

    def createAccount(self):
        self.name, self.pin, self.saldo=self.account
        self.name="Paolo"
        self.pin=1234
        self.saldo=100
        bank.add((self.name, self.pin, self.saldo))

#funzioni per avviare il programma
bank=Bank()
bank.add(("Paolo", 1234, 100))
bank.add(("Marco", 8000, 20))
bank.add(("Luca", 1859, 467))
def main():
    atm=ATM(bank)
    atm.mainloop()
    bank.save()
main()
