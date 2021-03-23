from turtle import Turtle, Screen
from numpy import *
import math
from decimal import Decimal as dec

class Campo_gravitazionale(Turtle):

    def __init__(self):

        Turtle.__init__(self)
        Turtle.hideturtle(self)
        self.t=Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.input()

    def input(self):
        self.lista_corpi=[]
        self.coordinate_punto=[]
        self.altezza=900
        self.lunghezza=1650
        self.risultati_finali=[]
        self.counter=0
        self.contatore_finale=0
        while True:
            try:
                x=int(input("ascissa corpo "+str(len(self.lista_corpi)+1)+": "))
                y=int(input("ordinata corpo "+str(len(self.lista_corpi)+1)+": "))
                carica=int(input("carica corpo "+str(len(self.lista_corpi)+1)+": "))
                carica*=-1
                print("\n")
                tmp_list=[x, y, carica]
                self.lista_corpi.append(tmp_list)
            except:
                break

        self.analizza_corpi()

    def analizza_corpi(self):
        max_x=0
        max_y=0
        max_carica=0
        self.massimi=[max_x, max_y, max_carica]
        for i in range(3):
            for corpo in self.lista_corpi:
                if abs(corpo[i])>abs(self.massimi[i]):
                    self.massimi[i]=corpo[i]

        self.change_coordinates_foraxes()

    def change_coordinates_foraxes(self):
        x_max=(self.lunghezza/2)/abs(self.massimi[0])
        y_max=(self.altezza/2)/abs(self.massimi[1])
        self.moltiplicatore_carica=50/abs(self.massimi[2])
        if x_max>=y_max:
            self.moltiplicatore_coord=y_max
        if x_max<y_max:
            self.moltiplicatore_coord=x_max

        for i in range(2):
            for corpo in self.lista_corpi:
                corpo[i]*=self.moltiplicatore_coord

        for corpo in self.lista_corpi:
            corpo[2]*=self.moltiplicatore_carica

        self.disegna_assi()
        self.disegna_corpi()

        self.calcola_ogni_punto1()


    def disegna_assi(self):
        #grandezza schermo: 1600x900

        self.t.up()
        self.t.goto(-self.lunghezza/2, 0)
        self.t.seth(0)
        self.t.down()
        self.t.forward(self.lunghezza)

        self.t.seth(135)
        self.t.forward(10)
        self.t.seth(315)
        self.t.forward(10)
        self.t.seth(225)
        self.t.forward(10)
        self.t.up()

        self.t.goto(0, -self.altezza/2)
        self.t.seth(90)
        self.t.down()
        self.t.forward(self.altezza)
        self.t.seth(225)
        self.t.forward(10)
        self.t.seth(45)
        self.t.forward(10)
        self.t.seth(315)
        self.t.forward(10)

        self.t.up()
        self.t.goto(self.lunghezza/2-20, 20)
        self.t.write("x", font=('Calibri', 15))

        self.t.goto(20, self.altezza/2-15)
        self.t.write('y', font=('Calibri', 15))

        self.t.up()
        self.disegna_corpi()

    def disegna_corpi(self):
        count=1
        for corpo in self.lista_corpi:
            self.t.goto(corpo[0], corpo[1])
            self.t.dot(abs(corpo[2]), "black")
            self.t.goto(corpo[0]+20, corpo[1]+20)
            self.t.write("m"+str(count)+" ( "+str(round(corpo[0]/(self.moltiplicatore_coord+0.0000000000000001)))+", "+\
            str(round(corpo[1]/(self.moltiplicatore_coord+0.0000000000000001)))+", "+str(round(corpo[2]/self.moltiplicatore_carica*-1))+" )")
            count+=1


    def calcola_ogni_punto1(self):
        self.separatore=500#17
        self.casi_totali=self.lunghezza*self.altezza/(self.separatore**2)
        for i in range(round(-self.lunghezza/2), round(self.lunghezza/2), self.separatore):
            for j in range(round(-self.altezza/2), round(self.altezza/2), self.separatore):
                self.coordinate_punto=[i, j]
                self.calcola_campi()


    def calcola_ogni_punto2(self):
        self.separatore=50#28
        self.casi_totali=self.lunghezza*self.altezza/(self.separatore**2)
        for i in range(round(-self.lunghezza/2), round(self.lunghezza/2), self.separatore):
            for j in range(round(-self.altezza/2), round(self.altezza/2), self.separatore):
                self.coordinate_punto=[i, j]
                self.calcola_campi()


    def calcola_campi(self):
        self.lista_campi=[]
        for corpo in self.lista_corpi:
            d_quadro=((corpo[0]/(self.moltiplicatore_coord+0.0000000000000001))-(self.coordinate_punto[0]/(self.moltiplicatore_coord+0.0000000000000001)))**2+\
            ((corpo[1]/(self.moltiplicatore_coord+0.0000000000000001))-(self.coordinate_punto[1]/(self.moltiplicatore_coord+0.0000000000000001)))**2
            g=dec((8.987551787368176*10**9)*(corpo[2]/self.moltiplicatore_carica+0.0000000000000001)/d_quadro)
            self.lista_campi.append(g)

        self.calcola_angoli()


    def calcola_angoli(self):
        self.lista_angoli=[]

        for corpo in self.lista_corpi:
            angolo= dec(arctan((corpo[1]-(self.coordinate_punto[1]))/((corpo[0]-(self.coordinate_punto[0]))+0.0000000000000001)))#in radianti
            self.lista_angoli.append(abs(angolo))

        self.calcola_componenti_campi()

    def calcola_componenti_campi(self):
        self.lista_campi_x=[]
        self.lista_campi_y=[]
        moltiplicatore_neg_pos=1
        count=0

        for campo in self.lista_campi:
            if self.lista_corpi[count][0]-self.coordinate_punto[0]<0:
                moltiplicatore_neg_pos=-1
            if self.lista_corpi[count][0]-self.coordinate_punto[0]>=0:
                moltiplicatore_neg_pos=1
            self.lista_campi_x.append((campo*dec(cos(float(self.lista_angoli[count]))))*moltiplicatore_neg_pos)
            count+=1
        count=0
        for campo in self.lista_campi:
            if self.lista_corpi[count][1]-self.coordinate_punto[1]<0:
                moltiplicatore_neg_pos=-1
            if self.lista_corpi[count][1]-self.coordinate_punto[1]>=0:
                moltiplicatore_neg_pos=1
            self.lista_campi_y.append((campo*dec(sin(float(self.lista_angoli[count]))))*moltiplicatore_neg_pos)
            count+=1

        self.calcola_campo_tot()

    def calcola_campo_tot(self):
        self.componente_campo_x=dec(0)
        self.componente_campo_y=dec(0)

        for campo in self.lista_campi_x:
            self.componente_campo_x+=campo
        for campo in self.lista_campi_y:
            self.componente_campo_y+=campo


        self.campo_tot=dec(math.sqrt((self.componente_campo_x)**2+(self.componente_campo_y)**2))

        self.calcola_angolo_finale()

    def calcola_angolo_finale(self):
        self.angolo_finale=dec(arctan(float(self.componente_campo_y/self.componente_campo_x)))
        self.angolo_finale=self.angolo_finale*dec(180/math.pi)
        self.salva_risultato()

    def salva_risultato(self):
        self.risultati_finali.append([self.campo_tot, self.coordinate_punto, \
        self.componente_campo_x, self.componente_campo_y, self.angolo_finale])

        '''
        campo_tot           0
        coordiante_punto       1
        componente_campo_x  2
        componente_campo_y  3
        angolo_finale    4
        '''

        if len(self.risultati_finali)>self.casi_totali:
            self.campo_max=0
            self.campo_min=1e10000
            for i in self.risultati_finali:
                if i[0]>self.campo_max:
                    self.campo_max=i[0]
                if i[0]<self.campo_min:
                    self.campo_min=i[0]
            if self.contatore_finale==0:
                self.disegna_vettori1()
            if self.contatore_finale==1:
                self.disegna_vettori2()
        else:
            print(len(self.risultati_finali), self.casi_totali)

    def disegna_vettori1(self):

        for risultati in self.risultati_finali:
            color=self.scegli_colore1(risultati)
            self.t.goto(risultati[1][0], risultati[1][1])
            self.t.dot(23, color)

        self.disegna_assi()
        self.disegna_corpi()

        self.risultati_finali=[]
        self.contatore_finale=1
        self.calcola_ogni_punto2()

    def scegli_colore1(self, risultati):
        differenza=dec(self.campo_max-self.campo_min)
        step=dec(differenza/4037912)#somma di quelli sotto
        if risultati[0]<(self.campo_min+step*2):
            return "dark violet"#(100, 100, 255)
        if risultati[0]>(self.campo_min+step*2) and risultati[0]<(self.campo_min+step*dec(6)):
            return "blue"#(50, 50, 255)
        if risultati[0]>(self.campo_min+step*dec(6)) and risultati[0]<(self.campo_min+step*dec(24)):
            return "dodger blue"#(50, 50, 255)
        if risultati[0]>(self.campo_min+step*dec(24)) and risultati[0]<(self.campo_min+step*dec(120)):
            return "aqua"#(50, 50, 255)
        if risultati[0]>(self.campo_min+step*dec(120)) and risultati[0]<(self.campo_min+step*dec(720)):
            return "lime"#(0, 0, 255)
        if risultati[0]>(self.campo_min+step*dec(720)) and risultati[0]<(self.campo_min+step*dec(5040)):
            return "green yellow"#(0, 0, 255)
        if risultati[0]>(self.campo_min+step*dec(5040)) and risultati[0]<(self.campo_min+step*dec(40320)):
            return "yellow"#(100, 0, 255)
        if risultati[0]>(self.campo_min+step*dec(40320)) and risultati[0]<(self.campo_min+step*dec(362880)):
            return "gold"#(200, 0, 255)
        if risultati[0]>(self.campo_min+step*dec(362880)) and risultati[0]<(self.campo_min+step*dec(3628800)):
            return "orange red"#(255, 0, 255)
        if risultati[0]>(self.campo_min+step*dec(3628800)):
            return "red"#(255, 0, 150)

    def disegna_vettori2(self):

        for risultati in self.risultati_finali:
            lunghezza_freccia=25

            self.t.goto(risultati[1][0], risultati[1][1])
            if risultati[2]>0 and risultati[3]>0:
                self.t.seth(float(risultati[4]))
                self.t.down()
                self.t.forward(lunghezza_freccia)
                self.t.seth(float(risultati[4])+float(135))
                self.t.forward(4)
                self.t.seth(float(risultati[4])-float(45))
                self.t.forward(4)
                self.t.seth(float(risultati[4])+float(225))
                self.t.forward(4)
                self.t.up()
            if risultati[2]<0 and risultati[3]>0:
                self.t.seth(float(180)+float(risultati[4]))
                self.t.down()
                self.t.forward(lunghezza_freccia)
                self.t.seth(float(risultati[4])+float(315))
                self.t.forward(4)
                self.t.seth(float(risultati[4])+float(135))
                self.t.forward(4)
                self.t.seth(float(risultati[4])+float(45))
                self.t.forward(4)
                self.t.up()
            if risultati[2]<0 and risultati[3]<0:
                self.t.seth(float(180)+float(risultati[4]))
                self.t.down()
                self.t.forward(lunghezza_freccia)
                self.t.seth(float(risultati[4])+float(315))
                self.t.forward(4)
                self.t.seth(float(risultati[4])+float(135))
                self.t.forward(4)
                self.t.seth(float(risultati[4])+float(45))
                self.t.forward(4)
                self.t.up()
            if risultati[2]>0 and risultati[3]<0:
                self.t.seth(float(risultati[4]))
                self.t.down()
                self.t.forward(lunghezza_freccia)
                self.t.seth(float(risultati[4])-float(135))
                self.t.forward(4)
                self.t.seth(float(risultati[4])+float(45))
                self.t.forward(4)
                self.t.seth(float(risultati[4])-float(225))
                self.t.forward(4)
                self.t.up()

        self.disegna_assi()
        self.disegna_corpi()




Campo_gravitazionale()
fine=input('>>> ')
