from tkinter import *
import math

class AreaDelCerchio(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Area del cerchio")
        self.grid()

        #campo per il raggio
        self.raggioLabel=Label(self, text="Raggio: ")
        self.raggioLabel.grid(row=0, column=0)
        self.radiusVar=DoubleVar()
        self.radiusEntry=Entry(self, textvariable=self.radiusVar)
        self.radiusEntry.grid(row=0, column=1)

        #campo per l'area
        self.arealabel=Label(self, text="Area: ")
        self.arealabel.grid(row=1, column=0)
        self.areaVar=DoubleVar()
        self.areaEntry=Entry(self, textvariable=self.areaVar)
        self.areaEntry.grid(row=1, column=1)

        #comando
        self.commandButton=Button(self, text="Compute", command=self.area)
        self.commandButton.grid(row=2, column=0, columnspan=2)

    def area(self):
        radius=self.radiusVar.get()
        area=radius**2*math.pi
        self.areaVar.set(area)
        
def main():
    AreaDelCerchio().mainloop()

main()
