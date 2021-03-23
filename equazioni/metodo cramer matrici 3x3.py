from tkinter import *
import tkinter

class Sistema(Frame):

    def __init__(self):
        Frame.__init__(self)

        self.master.title("metodo di cramer")
        self.grid()

        self.label1=Label(self, text="prima equazione: ")
        self.label2=Label(self, text="seconda equazione: ")
        self.label3=Label(self, text="terza equazione: ")

        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)
        self.label3.grid(row=2, column=0)

        self.primaVar=StringVar()
        self.secondaVar=StringVar()
        self.terzaVar=StringVar()

        self.primaEntry=Entry(self, textvariable=self.primaVar)
        self.secondaEntry=Entry(self, textvariable=self.secondaVar)
        self.terzaEntry=Entry(self, textvariable=self.terzaVar)

        self.primaEntry.grid(row=0, column=1)
        self.secondaEntry.grid(row=1, column=1)
        self.terzaEntry.grid(row=2, column=1)

        self.lista_equazioni=[]

        self.compari_lista_equazioniButton=Button(self, text="compute", command=self.componi_lista_equazioni)
        self.compari_lista_equazioniButton.grid(row=1, column=2)

        self.risposta0=False
        self.risposta1=False
        self.risopsta2=False
        self.risposta3=False#serve quando calcolo i risultati finali

        self.contatore=1#serve in trova_matrici()

    def componi_lista_equazioni(self):
        self.lista_equazioni.append(self.primaEntry.get())
        self.lista_equazioni.append(self.secondaVar.get())
        self.lista_equazioni.append(self.terzaVar.get())

        self.trova_matrici()

    def trova_matrici(self):

        self.matrice_label=Label(self, text="Matrice")
        self.matrice_label.grid(row=4, column=0, rowspan=2)

        for equazione in self.lista_equazioni:#considero un'equazione alla volta
            self.lista_elementi=equazione.split(" ")#creo una lista con i membri dell'equazione

            if self.contatore==1:
                self.lista_el_a=[]
                self.lista_el_b=[]
                self.lista_el_c=[]
                self.lista_termini_noti=[]

                for membro in self.lista_elementi:

                    if "x" in membro:
                        for el in membro:
                            self.lista_el_a.append(el)

                        self.lista_el_a.remove("x")

                    if "y" in membro:
                        for el in membro:
                            self.lista_el_b.append(el)

                        self.lista_el_b.remove("y")

                    if "z" in membro:
                        for el in membro:
                            self.lista_el_c.append(el)

                        self.lista_el_c.remove("z")


                    if "=" in membro:
                        for el in membro:
                            self.lista_termini_noti.append(el)

                        self.lista_termini_noti.remove("=")

                    self.coeff_a1="".join(self.lista_el_a)
                    self.coeff_b1="".join(self.lista_el_b)
                    self.coeff_c1="".join(self.lista_el_c)
                    self.term_noto1="".join(self.lista_termini_noti)


                    self.matrice_label1=Label(self, text=self.coeff_a1+" "+self.coeff_b1+" "+self.coeff_c1+"    "+self.term_noto1)
                    self.matrice_label1.grid(row=3, column=1)

            if self.contatore==2:
                self.lista_el_a=[]
                self.lista_el_b=[]
                self.lista_el_c=[]
                self.lista_termini_noti=[]

                for membro in self.lista_elementi:

                    if "x" in membro:
                        for el in membro:
                            self.lista_el_a.append(el)

                        self.lista_el_a.remove("x")

                    if "y" in membro:
                        for el in membro:
                            self.lista_el_b.append(el)

                        self.lista_el_b.remove("y")

                    if "z" in membro:
                        for el in membro:
                            self.lista_el_c.append(el)

                        self.lista_el_c.remove("z")

                    if "=" in membro:
                        for el in membro:
                            self.lista_termini_noti.append(el)

                        self.lista_termini_noti.remove("=")

                    self.coeff_a2="".join(self.lista_el_a)
                    self.coeff_b2="".join(self.lista_el_b)
                    self.coeff_c2="".join(self.lista_el_c)
                    self.term_noto2="".join(self.lista_termini_noti)

                    self.matrice_label2=Label(self, text=self.coeff_a2+" "+self.coeff_b2+" "+self.coeff_c2+"    "+self.term_noto2)
                    self.matrice_label2.grid(row=4, column=1)

            if self.contatore==3:
                self.lista_el_a=[]
                self.lista_el_b=[]
                self.lista_el_c=[]
                self.lista_termini_noti=[]

                for membro in self.lista_elementi:

                    if "x" in membro:
                        for el in membro:
                            self.lista_el_a.append(el)

                        self.lista_el_a.remove("x")

                    if "y" in membro:
                        for el in membro:
                            self.lista_el_b.append(el)

                        self.lista_el_b.remove("y")

                    if "z" in membro:
                        for el in membro:
                            self.lista_el_c.append(el)

                        self.lista_el_c.remove("z")

                    if "=" in membro:
                        for el in membro:
                            self.lista_termini_noti.append(el)

                        self.lista_termini_noti.remove("=")

                    self.coeff_a3="".join(self.lista_el_a)
                    self.coeff_b3="".join(self.lista_el_b)
                    self.coeff_c3="".join(self.lista_el_c)
                    self.term_noto3="".join(self.lista_termini_noti)

                    self.matrice_label3=Label(self, text=self.coeff_a3+" "+self.coeff_b3+" "+self.coeff_c3+"    "+self.term_noto3)
                    self.matrice_label3.grid(row=5, column=1)

            self.contatore+=1

        self.coeff_a1=int(self.coeff_a1)
        self.coeff_b1=int(self.coeff_b1)
        self.coeff_c1=int(self.coeff_c1)
        self.coeff_a2=int(self.coeff_a2)
        self.coeff_b2=int(self.coeff_b2)
        self.coeff_c2=int(self.coeff_c2)
        self.coeff_a3=int(self.coeff_a3)
        self.coeff_b3=int(self.coeff_b3)
        self.coeff_c3=int(self.coeff_c3)
        self.term_noto1=int(self.term_noto1)
        self.term_noto2=int(self.term_noto2)
        self.term_noto3=int(self.term_noto3)

        self.calcola_determinanti_button=Button(self, text="passa a calcolare i determinati", command=self.calcola_determinanti)
        self.calcola_determinanti_button.grid(row=6, column=0, columnspan=3)

    def calcola_determinanti(self):
        self.calcola_determinante_normale_button=Button(self, text="calcola il determinante principale", command=self.calcola_determinante_normale)
        self.calcola_determinante_normale_button.grid(row=7, column=0)

        self.calcola_determinante_x_button=Button(self, text="calcola il determinante x", command=self.calcola_determinante_x)
        self.calcola_determinante_x_button.grid(row=7, column=1)

        self.calcola_determinante_y_button=Button(self, text="calcola il determinante y", command=self.calcola_determinante_y)
        self.calcola_determinante_y_button.grid(row=7, column=2)

        self.calcola_determinante_z_button=Button(self, text="calcola il determinante z", command=self.calcola_determinante_z)
        self.calcola_determinante_z_button.grid(row=7, column=3)



    def calcola_determinante_normale(self):
        self.determinante_principale=(self.coeff_a1*self.coeff_b2*self.coeff_c3)+\
                           (self.coeff_b1*self.coeff_c2*self.coeff_a3)+\
                           (self.coeff_c1*self.coeff_a2*self.coeff_b3)-\
                           (self.coeff_a1*self.coeff_c2*self.coeff_b3)-\
                           (self.coeff_b1*self.coeff_a2*self.coeff_c3)-\
                           (self.coeff_c1*self.coeff_b2*self.coeff_a3)

        self.determinante_normale_label=Label(self, text="determinante principale: "+str(self.determinante_principale))
        self.determinante_normale_label.grid(row=8,column=0)

    def calcola_determinante_x(self):
        self.determinante_x=(self.term_noto1*self.coeff_b2*self.coeff_c3)+\
                           (self.coeff_b1*self.coeff_c2*self.term_noto3)+\
                           (self.coeff_c1*self.term_noto2*self.coeff_b3)-\
                           (self.term_noto1*self.coeff_c2*self.coeff_b3)-\
                           (self.coeff_b1*self.term_noto2*self.coeff_c3)-\
                           (self.coeff_c1*self.coeff_b2*self.term_noto3)

        self.determinante_x_label=Label(self, text="determinante x: "+str(self.determinante_x))
        self.determinante_x_label.grid(row=8,column=1)


    def calcola_determinante_y(self):
        self.determinante_y=(self.coeff_a1*self.term_noto2*self.coeff_c3)+\
                           (self.term_noto1*self.coeff_c2*self.coeff_a3)+\
                           (self.coeff_c1*self.coeff_a2*self.term_noto3)-\
                           (self.coeff_a1*self.coeff_c2*self.term_noto3)-\
                           (self.term_noto1*self.coeff_a2*self.coeff_c3)-\
                           (self.coeff_c1*self.term_noto2*self.coeff_a3)

        self.determinante_y_label=Label(self, text="determinante x: "+str(self.determinante_y))
        self.determinante_y_label.grid(row=8,column=2)

    def calcola_determinante_z(self):
        self.determinante_z=(self.coeff_a1*self.coeff_b2*self.term_noto3)+\
                           (self.coeff_b1*self.term_noto2*self.coeff_a3)+\
                           (self.term_noto1*self.coeff_a2*self.coeff_b3)-\
                           (self.coeff_a1*self.term_noto2*self.coeff_b3)-\
                           (self.coeff_b1*self.coeff_a2*self.term_noto3)-\
                           (self.term_noto1*self.coeff_b2*self.coeff_a3)

        self.determinante_z_label=Label(self, text="determinante principale: "+str(self.determinante_z))
        self.determinante_z_label.grid(row=8,column=3)

        self.final_button=Button(self, text="calcola le incongnite", command=self.calcola_incognite)
        self.final_button.grid(row=9, column=0, columnspan=4)

    def calcola_incognite(self):
        self.calcolax_button=Button(self, text="Calcola la x", command=self.compari_x)
        self.calcolay_button=Button(self, text="Calcola la y", command=self.compari_y)
        self.calcolaz_button=Button(self, text="Calcola la y", command=self.compari_z)

        self.calcolax_button.grid(row=10, column=0)
        self.calcolay_button.grid(row=11, column=0)
        self.calcolaz_button.grid(row=12, column=0)

    def compari_x(self):
        self.x=self.determinante_x/self.determinante_principale
        self.label_x=Label(self, text="La x è "+str(self.x))
        self.label_x.grid(row=10, column=1)

    def compari_y(self):
        self.y=self.determinante_y/self.determinante_principale
        self.label_y=Label(self, text="La y è "+str(self.y))
        self.label_y.grid(row=11, column=1)

    def compari_z(self):
        self.z=self.determinante_z/self.determinante_principale
        self.label_z=Label(self, text="La z è "+str(self.z))
        self.label_z.grid(row=12, column=1)



def main():
    Sistema().mainloop()
main()
