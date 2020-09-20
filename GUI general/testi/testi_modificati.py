from tkinter import *
import tkinter
class Testi_colorati(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("Ciao")
        self.master.geometry("300x500")
        self.master.resizable(0, 1)
        self.textLabel=Label(self, text="Ciao")
        self.textLabel.grid()
def main():
    Testi_colorati().mainloop()
main()
