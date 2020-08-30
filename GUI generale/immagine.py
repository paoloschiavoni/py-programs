from tkinter import *
class ImageDemo(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Immagine")
        self.grid()
        self._image=PhotoImage(file="Penguins.jpg")
        self._imageLabel=Label(self, image=self.image)
        self.imageLabel.grid()
        self._textLabel=Label(self, text="ciao")
        self._textLabel.grid()

def main():
    ImageDemo().mainloop()

main()
