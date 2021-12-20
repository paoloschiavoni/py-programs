from tkinter import *
class TrisComputer(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.grid()

        self.master.title("Tris")

        self.b1=Button(self, text=" X  ")
        self.b2=Button(self, text="    ", command=self.change3)
        self.b3=Button(self, text="    ", command=self.change4)
        self.b4=Button(self, text="    ", command=self.change3)
        self.b5=Button(self, text="    ", command=self.change1)
        self.b6=Button(self, text="    ", command=self.change5)
        self.b7=Button(self, text="    ", command=self.change4)
        self.b8=Button(self, text="    ", command=self.change5)
        self.b9=Button(self, text="    ", command=self.change2)

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.statusLabel=Label(self, text="Tu sei O")
        self.statusLabel.grid(row=3, column=0, columnspan=3)
        self.resetButton=Button(self, text="Reset", command=self.reset)
        self.resetButton.grid(row=0, column=3)


    def change1(self):
        self.b5["text"]=" O  "

        #MOSSA DEL COMPTER
        self.b9["text"]=" X  "

        self.b3["command"]=self.change1_1
        self.b7["command"]=self.change1_1#lo stesso caso, ma speculare

        self.b2["command"]=self.change1_2
        self.b4["command"]=self.change1_2
        self.b6["command"]=self.change1_2
        self.b8["command"]=self.change1_2

    def change1_1(self):
        self.b3["text"]=" O  "

        #mossa del computer
        self.b7["text"]=" X  "

        self.b2["command"]=self.change1_1_1
        self.b6["command"]=self.change1_1_1

        self.b4["command"]=self.change1_1_2
        self.b8["command"]=self.change1_1_2


    def change1_1_1(self):
        self.b2["text"]=" O  "

        self.b4["text"]=" X  "
        self.statusLabel["text"]="Hai perso!"

    def change1_1_2(self):
        self.b8["text"]=" O  "

        self.b4["text"]=" X  "
        self.statusLabel["text"]="Hai perso!"

    def change1_2(self):
        self.b2["text"]=" O "

        self.b8["text"]=" X "
        self.b7["command"]=self.change1_2_1
        self.b4["command"]=self.change1_2_2
        self.b3["command"]=self.change1_2_2
        self.b6["command"]=self.change1_2_2

    def change1_2_1(self):
        self.b7["text"]=" O "
        self.b3["text"]=" X "
        self.statusLabel["text"]="Pareggio!"

    def change1_2_2(self):
        self.b4["text"]=" O "
        self.b7["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

#######################
####################### FINITO CHANGE 1
#######################

    def change2(self):
        self.b9["text"]=" O "

        self.b7["text"]=" X "

        self.b2["command"]=self.change2_1
        self.b3["command"]=self.change2_1
        self.b5["command"]=self.change2_1
        self.b6["command"]=self.change2_1
        self.b8["command"]=self.change2_1

        self.b4["command"]=self.change2_2

    def change2_1(self):
        self.b2["text"]=" O "

        self.b4["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change2_2(self):
        self.b4["text"]=" O "

        self.b3["text"]=" X "

        self.b2["command"]=self.change2_2_1
        self.b5["command"]=self.change2_2_2
        self.b6["command"]=self.change2_2_2
        self.b8["command"]=self.change2_2_2

    def change2_2_1(self):
        self.b2["text"]=" O "

        self.b5["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change2_2_2(self):
        self.b5["text"]=" O "

        self.b2["text"]=" X "
        self.statusLabel["text"]="Hai perso!"


###########################
########################### FINE CHANGE 2
##########################

    def change3(self):
        self.b2["text"]=" O "

        self.b5["text"]=" X "

        self.b3["command"]=self.change3_1
        self.b4["command"]=self.change3_1
        self.b6["command"]=self.change3_1
        self.b7["command"]=self.change3_1
        self.b8["command"]=self.change3_1

        self.b9["command"]=self.change3_2

    def change3_1(self):
        self.b3["text"]=" O "

        self.b9["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change3_2(self):
        self.b9["text"]=" O "

        self.b7["text"]=" X "
        self.b4["command"]=self.change3_2_1
        self.b3["command"]=self.change3_2_2
        self.b6["command"]=self.change3_2_2
        self.b8["command"]=self.change3_2_2

    def change3_2_1(self):
        self.b4["text"]=" O "

        self.b3["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change3_2_2(self):
        self.b3["text"]=" O "

        self.b4["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

#######################FINE CHANGE 3

    def change4(self):
        self.b3["text"]=" O "

        self.b9["text"]=" X "

        self.b2["command"]=self.change4_1
        self.b4["command"]=self.change4_1
        self.b6["command"]=self.change4_1
        self.b7["command"]=self.change4_1
        self.b8["command"]=self.change4_1

        self.b5["command"]=self.change4_2

    def change4_1(self):
        self.b2["text"]=" O "

        self.b5["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change4_2(self):
        self.b5["text"]=" O "

        self.b7["text"]=" X "

        self.b4["command"]=self.change4_2_1
        self.b2["command"]=self.change4_2_1
        self.b6["command"]=self.change4_2_1
        self.b8["command"]=self.change4_2_2

    def change4_2_1(self):
        self.b4["text"]=" O "

        self.b8["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change4_2_2(self):
        self.b8["text"]=" O "

        self.b4["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

############## FINE CHANGE 4

    def change5(self):
        self.b6["text"]=" O "

        self.b7["text"]=" X "

        self.b2["command"]=self.change5_1
        self.b3["command"]=self.change5_1
        self.b5["command"]=self.change5_1
        self.b8["command"]=self.change5_1
        self.b9["command"]=self.change5_1

        self.b4["command"]=self.change5_2

    def change5_1(self):
        self.b5["text"]=" O "

        self.b4["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change5_2(self):
        self.b4["text"]=" O "
        self.b5["text"]=" X "

        self.b2["command"]=self.change5_2_1
        self.b3["command"]=self.change5_2_1
        self.b8["command"]=self.change5_2_2
        self.b9["command"]=self.change5_2_2

    def change5_2_1(self):
        self.b3["text"]=" O "
        self.b9["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

    def change5_2_2(self):
        self.b9["text"]=" O "
        self.b3["text"]=" X "
        self.statusLabel["text"]="Hai perso!"

############# FINE CHANGE 5


    def reset(self):
        self.b1["text"]=" X "
        self.b2["text"]="    "
        self.b3["text"]="    "
        self.b4["text"]="    "
        self.b5["text"]="    "
        self.b6["text"]="    "
        self.b7["text"]="    "
        self.b8["text"]="    "
        self.b9["text"]="    "

        self.b2["command"]=command=self.change3
        self.b3["command"]=command=self.change4
        self.b4["command"]=command=self.change3
        self.b5["command"]=command=self.change1
        self.b6["command"]=command=self.change5
        self.b7["command"]=command=self.change4
        self.b8["command"]=command=self.change5
        self.b9["command"]=command=self.change2


        self.statusLabel["text"]="Bentornato!"





def main():
    print("Da quando ci sarà scritto che qualcuno vince, \nil gioco non andrà più avanti regolarmente, \
\ncliccare rest per rigiocare\n\nSe qualche mossa viene modificata, \
\nè perchè è speculare rispetto a quella fatta")
    TrisComputer().mainloop()
main()
