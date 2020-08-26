from tkinter import *
import tkinter
class TextDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Text Demo")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky= W+E+N+S)
        self.outputArea=Text(self, width=20, height=8, wrap=WORD)

        self.outputArea.grid(row=0, column=0, columnspan=2, sticky=W+E+N+S)

        self.showButton=Button(self, text="Show", command=self.show)
        self.showButton.grid(row=1, column=0)

        self.clearButton=Button(self, text="clear", command=self.clear)
        self.clearButton.grid(row=1, column=1)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def show(self):
        self.outputArea.insert("1.0", "ciao bello ")

    def clear(self):
        self.outputArea.delete("1.0", END)

def main():
    TextDemo().mainloop()
main()
