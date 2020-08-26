from tkinter import *
class Tris1v1(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.count=0

        self.master.title("Tris")
        
        self.b1=Button(self, text="    ", command=self.change1)
        self.b2=Button(self, text="    ", command=self.change2)
        self.b3=Button(self, text="    ", command=self.change3)
        self.b4=Button(self, text="    ", command=self.change4)
        self.b5=Button(self, text="    ", command=self.change5)
        self.b6=Button(self, text="    ", command=self.change6)
        self.b7=Button(self, text="    ", command=self.change7)
        self.b8=Button(self, text="    ", command=self.change8)
        self.b9=Button(self, text="    ", command=self.change9)

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)
        self.count+=1

        self.statusLabel=Label(self, text="Turno di O")
        self.statusLabel.grid(row=3, column=0, columnspan=3)

        self.resetButton=Button(self, text="Reset", command=self.reset)
        self.resetButton.grid(row=0, column=3)
        

    def change1(self):
        if self.count%2==0:
            self.b1["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b1["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b1["state"]=DISABLED
        
    def change2(self):
        if self.count%2==0:
            self.b2["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b2["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b2["state"]=DISABLED
        
    def change3(self):
        if self.count%2==0:
            self.b3["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b3["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b3["state"]=DISABLED
        
    def change4(self):
        if self.count%2==0:
            self.b4["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b4["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b4["state"]=DISABLED
        
    def change5(self):
        if self.count%2==0:
            self.b5["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b5["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b5["state"]=DISABLED
        
    def change6(self):
        if self.count%2==0:
            self.b6["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b6["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b6["state"]=DISABLED
        
    def change7(self):
        if self.count%2==0:
            self.b7["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b7["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b7["state"]=DISABLED
        
    def change8(self):
        if self.count%2==0:
            self.b8["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b8["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b8["state"]=DISABLED
        
    def change9(self):
        if self.count%2==0:
            self.b9["text"]=" X "
            self.statusLabel["text"]="Turno di O"
            self.winsX()
        else:
            self.b9["text"]=" O "
            self.statusLabel["text"]="Turno di X"
            self.winsO()
        self.count+=1
        self.b9["state"]=DISABLED
        

    def winsX(self):
        if self.b1["text"]==" X " and self.b2["text"]==" X " and self.b3["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b4["text"]==" X " and self.b5["text"]==" X " and self.b6["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b7["text"]==" X " and self.b8["text"]==" X " and self.b9["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b1["text"]==" X " and self.b4["text"]==" X " and self.b7["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b2["text"]==" X " and self.b5["text"]==" X " and self.b8["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b3["text"]==" X " and self.b6["text"]==" X " and self.b9["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b1["text"]==" X " and self.b5["text"]==" X " and self.b9["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b3["text"]==" X " and self.b5["text"]==" X " and self.b7["text"]==" X ":
            self.statusLabel["text"]="Vince X"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
            
    def winsO(self):
        if self.b1["text"]==" O " and self.b2["text"]==" O " and self.b3["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b4["text"]==" O " and self.b5["text"]==" O " and self.b6["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b7["text"]==" O " and self.b8["text"]==" O " and self.b9["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b1["text"]==" O " and self.b4["text"]==" O " and self.b7["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b2["text"]==" O " and self.b5["text"]==" O " and self.b8["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b3["text"]==" O " and self.b6["text"]==" O " and self.b9["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b1["text"]==" O " and self.b5["text"]==" O " and self.b9["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED
        if self.b3["text"]==" O " and self.b5["text"]==" O " and self.b7["text"]==" O ":
            self.statusLabel["text"]="Vince O"
            self.b1["state"]=DISABLED
            self.b2["state"]=DISABLED
            self.b3["state"]=DISABLED
            self.b4["state"]=DISABLED
            self.b5["state"]=DISABLED
            self.b6["state"]=DISABLED
            self.b7["state"]=DISABLED
            self.b8["state"]=DISABLED
            self.b9["state"]=DISABLED


    def reset(self):
        self.b1["text"]="    "
        self.b2["text"]="    "
        self.b3["text"]="    "
        self.b4["text"]="    "
        self.b5["text"]="    "
        self.b6["text"]="    "
        self.b7["text"]="    "
        self.b8["text"]="    "
        self.b9["text"]="    "
        
        self.b1["state"]=NORMAL
        self.b2["state"]=NORMAL
        self.b3["state"]=NORMAL
        self.b4["state"]=NORMAL
        self.b5["state"]=NORMAL
        self.b6["state"]=NORMAL
        self.b7["state"]=NORMAL
        self.b8["state"]=NORMAL
        self.b9["state"]=NORMAL

        if self.count%2==0:
            self.statusLabel["text"]="Turno di O"
        else:
            self.statusLabel["text"]="Turno di X"

def main():
    Tris1v1().mainloop()
main()