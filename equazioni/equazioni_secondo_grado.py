from tkinter import *
import tkinter
import math

class Equazione_secondo_grado(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("equazione di secondo grando")
        self.grid()

        self.label_equazione=Label(self, text="equazione: ")
        self.label_equazione.grid(row=0, column=0)

        self.equazioneVar=StringVar()
        self.equazione_entry=Entry(self, textvariable=self.equazioneVar)
        self.equazione_entry.grid(row=0, column=1, columnspan=2)

        self.calcola_coefficienti_button=Button(self, text="compute", command=self.calcola_coefficienti)
        self.calcola_coefficienti_button.grid(row=1, column=1)
        
    def calcola_coefficienti(self):
        self.lista_elementi=[]
        self.lista_elementi=self.equazioneVar.get().split(" ")

        self.lista_a=[]
        self.lista_b=[]
        self.lista_c=[]
        
        for el in self.lista_elementi:

            if "x**2"in el:
                for num in el:
                    self.lista_a.append(num)
                for count in range(3):
                    self.lista_a.pop()
                self.coeff_a=int("".join(self.lista_a))
                
            if not "x**2" in el and "x"in el:
                for num in el:
                    self.lista_b.append(num)
                self.lista_b.pop()
                self.coeff_b=int("".join(self.lista_b))

            if not "x" in el and not "=" in el:
                self.coeff_c=int(el)

            if "=" in el:
                self.lista_elementi.remove(el)

        self.a_label=Label(self, text="a = "+str(self.coeff_a))
        self.a_label.grid(row=2, column=0)
        
        self.b_label=Label(self, text="b = "+str(self.coeff_b))
        self.b_label.grid(row=3, column=0)
        
        self.c_label=Label(self, text="c = "+str(self.coeff_c))
        self.c_label.grid(row=4, column=0)

        self.calcola_discriminante_button=Button(self, text="calcola il discriminante", command=self.calcola_discriminante)
        self.calcola_discriminante_button.grid(row=5, column=0)

    def calcola_discriminante(self):
        self.discriminante=(self.coeff_b**2) - (4*self.coeff_a*self.coeff_c)

        self.discriminante_label=Label(self, text="il discriminante è "+str(self.discriminante))
        self.discriminante_label.grid(row=6, column=0)

        if self.discriminante == 0:
            self.caratteristica_d_label=Label(self, text="= 0 -> due radici coincidenti")
            self.caratteristica_d_label.grid(row=6, column=1)

            self.calcola_radici_button=Button(self, text="calcola le radici", command=self.calcola_radici)
            self.calcola_radici_button.grid(row=7, column=0)
        
        if self.discriminante <0:
            self.caratteristica_d_label=Label(self, text="< 0 -> nessuna radice")
            self.caratteristica_d_label.grid(row=6, column=1)
        
        if self.discriminante >0:
            self.caratteristica_d_label=Label(self, text="> 0 -> due radici distinte")
            self.caratteristica_d_label.grid(row=6, column=1)
            
            self.calcola_radici_button=Button(self, text="calcola le radici", command=self.calcola_radici)
            self.calcola_radici_button.grid(row=7, column=0)

    def calcola_radici(self):
        self.radice1=(-self.coeff_b + math.sqrt(self.discriminante)) / (2*self.coeff_a)
        self.radice2=(-self.coeff_b - math.sqrt(self.discriminante)) / (2*self.coeff_a)

        self.radice_label1=Label(self, text="la radice 1 è "+str(self.radice1))
        self.radice_label2=Label(self, text="la radice 2 è "+str(self.radice2))

        self.radice_label1.grid(row=8, column=0)
        self.radice_label2.grid(row=9, column=0)


def main():
    Equazione_secondo_grado().mainloop()
main()
