from tkinter import *
class ListBox(Frame):

    def __init__(self):
        Frame.__init__(self)
        self._listPane=Frame(self)
        self.grid()
        self.master.title("ListBox")

        self._listPane.grid(row=0, column=0, sticky=N+S)
        self.yScroll=Scrollbar(self._listPane, orient=VERTICAL)
        self.yScroll.grid(row=0, column=1, sticky=N+S)

        self.theList=Listbox(self._listPane, width=5, height=10, selectmode=SINGLE, yscrollcommand=self.yScroll)
        self.theList.grid(row=0, column=0, sticky=N+S)
        self.yScroll["command"]=self.theList.yview

        self.theList.insert(END, "ciao")
        
        
def main():
    ListBox().mainloop()
main()
