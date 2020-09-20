from tkinter import *

class LabelDemo(Frame):

    def __init__(self):
        #imposta la finisetra e i suoi oggetti
        Frame.__init__(self)
        self.master.title("A caso")
        self.grid()
        self._label=Label(self, text ="Bella raga")
        self._label.grid()

def main():
    #visulaizza la finestra
    LabelDemo().mainloop()

main()
