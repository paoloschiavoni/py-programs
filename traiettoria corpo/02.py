from turtle import Turtle, Screen
from numpy import *
import math
from decimal import Decimal as dec

class Traiettoria(Turtle):

    def __init__(self):

        Turtle.__init__(self)
        Turtle.hideturtle(self)
        self.t=Turtle()
        self.t.hideturtle()
        self.t.speed(0)

        self.input()
        self.analizza_corpi()
        self.change_coordinates_foraxes()
        self.disegna_assi()
        self.disegna_corpi()
        self.disegna_punto()

    def input(self):
        self.lista_corpi=[]
        self.info_punto=[]
        self.altezza=300#da ripicciolire o ingrandire per rimpicciolire o ingrandire il grafico
        self.lunghezza=550
        self.altezza_foraxes=900#quelle per disegnare gli assi
        self.lunghezza_foraxes=1650

        dati=open("dati.txt")
        dati=dati.read()

        dati=dati.split("\n")

        vyp=int(dati[-2])
        vxp=int(dati[-3])
        yp=int(dati[-4])
        xp=int(dati[-5])

        self.info_punto.append(xp)
        self.info_punto.append(yp)
        self.info_punto.append(vxp)
        self.info_punto.append(vyp)

        for count in range(6):
            dati.pop(-1)

        x=0
        y=0
        massa=0

        for dato in dati:
            if dati.index(dato) %3==0:
                x=int(dato)
            if dati.index(dato) %3==1:
                y=int(dato)
            if dati.index(dato) %3==2:
                massa=int(dato)
                self.lista_corpi.append([x, y, massa])

    def analizza_corpi(self):
        max_x=0
        max_y=0
        max_massa=0
        self.massimi=[max_x, max_y, max_massa]
        for i in range(3):
            for corpo in self.lista_corpi:
                if abs(corpo[i])>abs(self.massimi[i]):
                    self.massimi[i]=abs(corpo[i])

        if abs(self.info_punto[0])>abs(self.massimi[0]):
            self.massimi[0]=self.info_punto[0]
        if abs(self.info_punto[1])>abs(self.massimi[1]):
            self.massimi[1]=self.info_punto[1]


    def change_coordinates_foraxes(self):
        x_max=(self.lunghezza/2)/(self.massimi[0]+0.0000000000000001)
        y_max=(self.altezza/2)/(self.massimi[1]+0.0000000000000001)
        self.moltiplicatore_massa=20/(self.massimi[2]+0.0000000000000001)

        if x_max>=y_max:
            self.moltiplicatore_coord=y_max
        if x_max<y_max:
            self.moltiplicatore_coord=x_max

        for i in range(2):
            for corpo in self.lista_corpi:
                corpo[i]*=self.moltiplicatore_coord

        for corpo in self.lista_corpi:
            corpo[2]*=self.moltiplicatore_massa

        self.info_punto[0]*=abs(self.moltiplicatore_coord)
        self.info_punto[1]*=abs(self.moltiplicatore_coord)
        self.info_punto[2]*=abs(self.moltiplicatore_coord)
        self.info_punto[3]*=abs(self.moltiplicatore_coord)



    def disegna_assi(self):

        self.t.up()
        self.t.goto(-self.lunghezza_foraxes/2, 0)
        self.t.seth(0)
        self.t.down()
        self.t.forward(self.lunghezza_foraxes)

        self.t.seth(135)
        self.t.forward(10)
        self.t.seth(315)
        self.t.forward(10)
        self.t.seth(225)
        self.t.forward(10)
        self.t.up()

        self.t.goto(0, -self.altezza_foraxes/2)
        self.t.seth(90)
        self.t.down()
        self.t.forward(self.altezza_foraxes)
        self.t.seth(225)
        self.t.forward(10)
        self.t.seth(45)
        self.t.forward(10)
        self.t.seth(315)
        self.t.forward(10)

        self.t.up()
        self.t.goto(self.lunghezza_foraxes/2-20, 20)
        self.t.write("x", font=('Calibri', 15))

        self.t.goto(20, self.altezza_foraxes/2-15)
        self.t.write('y', font=('Calibri', 15))

        self.t.up()


    def disegna_corpi(self):
        count=1
        for corpo in self.lista_corpi:
            self.t.goto(corpo[0], corpo[1])
            self.t.dot(corpo[2], "black")
            self.t.goto(corpo[0]+20, corpo[1]+20)
            self.t.write("m"+str(count)+\
            " ( "+str(corpo[0]/(self.moltiplicatore_coord+0.0000000000000001))+\
            ", "+str(corpo[1]/(self.moltiplicatore_coord+0.0000000000000001))+" )")
            self.t.up()
            self.t.goto(round(self.info_punto[0]), round(self.info_punto[1]))
            self.t.down()
            self.t.speed(2)
            count+=1


    def disegna_punto(self):
        if self.continua_traiettoria():
            self.t.goto(round(self.info_punto[0]), round(self.info_punto[1]))
            self.nuovo_punto()

    def continua_traiettoria(self):
        for corpo in self.lista_corpi:
            if self.info_punto[0]<(corpo[0]+5) and self.info_punto[0]>(corpo[0]-5):
                if self.info_punto[1]<(corpo[1]+5) and self.info_punto[1]>(corpo[0]-5):
                    self.t.up()
                    while 1:
                        self.t.forward(1)
                    return False
        else:
            return True


    def nuovo_punto(self):
        self.calcola_campi()
        self.calcola_angoli()
        self.calcola_componenti_campi()
        self.calcola_campo_tot()
        self.calcola_angolo_finale()

        self.info_punto[2]+=float(self.componente_campo_x*dec(self.moltiplicatore_coord))
        self.info_punto[3]+=float(self.componente_campo_y*dec(self.moltiplicatore_coord))

        self.info_punto[0]+=(self.info_punto[2])
        self.info_punto[1]+=(self.info_punto[3])

        self.disegna_punto()

    def calcola_campi(self):
        self.lista_campi=[]
        for corpo in self.lista_corpi:
            d_quadro=((corpo[0]/(self.moltiplicatore_coord+0.0000000000000001))-(self.info_punto[0]/(self.moltiplicatore_coord+0.0000000000000001)))**2+\
            ((corpo[1]/(self.moltiplicatore_coord+0.0000000000000001))-(self.info_punto[1]/(self.moltiplicatore_coord+0.0000000000000001)))**2
            g=dec(6.67*(10**-11)*(corpo[2]/(self.moltiplicatore_massa+0.0000000000000001))/(d_quadro+0.0000000000000001))
            self.lista_campi.append(g)


    def calcola_angoli(self):
        self.lista_angoli=[]

        for corpo in self.lista_corpi:
            angolo= dec(arctan((corpo[1]-self.info_punto[1])/((corpo[0]-self.info_punto[0])+0.0000000000000001)))#in radianti
            self.lista_angoli.append(abs(angolo))


    def calcola_componenti_campi(self):
        self.lista_campi_x=[]
        self.lista_campi_y=[]
        moltiplicatore_neg_pos=1
        count=0


        for campo in self.lista_campi:
            if self.lista_corpi[count][0]-self.info_punto[0]<0:
                moltiplicatore_neg_pos=-1
            if self.lista_corpi[count][0]-self.info_punto[0]>=0:
                moltiplicatore_neg_pos=1
            self.lista_campi_x.append((campo*dec(cos(float(self.lista_angoli[count]))))*moltiplicatore_neg_pos)
            count+=1
        count=0
        for campo in self.lista_campi:
            if self.lista_corpi[count][1]-self.info_punto[1]<0:
                moltiplicatore_neg_pos=-1
            if self.lista_corpi[count][1]-self.info_punto[1]>=0:
                moltiplicatore_neg_pos=1
            self.lista_campi_y.append((campo*dec(sin(float(self.lista_angoli[count]))))*moltiplicatore_neg_pos)
            count+=1


    def calcola_campo_tot(self):
        self.componente_campo_x=dec(0)
        self.componente_campo_y=dec(0)

        for campo in self.lista_campi_x:
            self.componente_campo_x+=campo
        for campo in self.lista_campi_y:
            self.componente_campo_y+=campo


        self.campo_tot=dec(math.sqrt((self.componente_campo_x)**2+(self.componente_campo_y)**2))


    def calcola_angolo_finale(self):
        self.angolo_finale=dec(arctan(float(self.componente_campo_y/self.componente_campo_x)))
        self.angolo_finale=self.angolo_finale*dec(180/math.pi)

Traiettoria()
fine=input('>>> ')
