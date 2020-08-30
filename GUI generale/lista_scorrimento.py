from tkinter import *
class ListDemo(Frame):

    def __init__(self):
        Frame.__init__(self)
        self._listPane=Frame(self)
        self.grid()
        self.master.title("List Box Demo")
        self._listPane.grid(row=0, column=0, sticky=N+S)

        self.yScroll=Scrollbar(self._listPane, orient=VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=N+S)

        self.theList=Listbox(self._listPane, width=10, height=5, selectmode=SINGLE, yscrollcommand=self.yScroll.set)
        self.theList.grid(row=0, column=0, sticky=N+S)
        self.yScroll["command"]=self.theList.yview

        self.rowconfigure(0, weight=1)
        self._listPane.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self._listPane.columnconfigure(0, weight=1)

        self.theList.insert(END, "a")
        self.theList.insert(END, "b")
        self.theList.insert(END, "c")
        self.theList.insert(END, "d")
        self.theList.insert(END, "f")
        self.theList.insert(END, "g")
        self.theList.insert(END, "h")
        self.theList.activate(0)

        self.removeButton=Button(self, text="Remove", command=self.remove)
        self.removeButton.grid(row=1, column=1)

        #aggiunge la stringa alla lista e la visualizza
        self.nuovaStringaVar=StringVar()
        self.nuovaStringaEntry=Entry(self, textvariable=self.nuovaStringaVar)
        self.nuovaStringaEntry.grid(row=0, column=1)
        self.addButton=Button(self, text="Add", command=self.add)
        self.addButton.grid(row=0, column=2)

    def add(self):
        self.theList.insert(END, self.nuovaStringaVar.get())
        self.theList.see(END)
        self.nuovaStringaVar.set("")

    
    def remove(self):
        #se e selezionata una lista la rimuove
        if self.theList.size()>0:
            self.theList.delete(ACTIVE)
def main():
    ListDemo().mainloop()
main()
