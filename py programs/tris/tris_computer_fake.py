from tkinter import *
class TrisComputer(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.count=0

        self.master.title("Tu sei O")
        
        self.b1=Button(self, text=" X ", state=DISABLED)
        self.b2=Button(self, text="    ")
        self.b3=Button(self, text="    ")
        self.b4=Button(self, text="    ")
        self.b5=Button(self, text="    ", command=self.change1)
        self.b6=Button(self, text="    ")
        self.b7=Button(self, text="    ")
        self.b8=Button(self, text="    ")
        self.b9=Button(self, text="    ")

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.statusLabel=Label(self, text="Se la tua \nmossa non \nè quella del \ncomputer, è \nperchè è speculare!")
        self.statusLabel.grid(row=3, column=0, columnspan=3)


    def change1(self):
        self.b5["text"]=" O "
        self.b5["state"]=DISABLED

        #MOSSA DEL COMPTER
        self.b9["text"]=" X "
        self.b9["state"]=DISABLED

        self.b3["command"]=self.change1_1
        self.b7["command"]=self.change1_1#lo stesso caso, ma speculare

    def change1_1(self):
        self.b3["text"]=" O "
        self.b3["state"]=DISABLED

        #mossa del computer
        self.b7["text"]=" X "
        self.b7["state"]=DISABLED
def main():
    TrisComputer().mainloop()
main()
        
