from tkinter import *
class Bottone(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.master.title("Bottone")
        self.grid()
        self._label=Label(self, text="Ecco un bottone")
        self._label.grid()
        self._button= Button(self, text="clicca qui", command =self._switch)
        self._button.grid()

    def _switch(self):
        #gestisce gli eventi

        if self._label["text"]=="Ecco un bottone":
            self._label["text"] =  "bravo!"
        else:
            self._label["text"]= "Ecco un bottone"

def main():
    Bottone().mainloop()

main()