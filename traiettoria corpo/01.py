'''
schiavoni paolo
questo programma disegna la traiettoria di un punto materiale intorno a dei corpi.
la massa dei corpi influneza la traiettoria del punto tramite il loro campo gravitazionale

organizzare i dati, nel file dati.txt così:

1 x corpo 1
2 y corpo 1
3  massa corpo 1
4 x corpo n
5 y corpo n
6 massa corpo n
7
8 x punto
9 y punto
10 velocità x punto
11 velocità y punto
12
13 spostamento massimo
14 raggio pianeti(pixel)

lo spostamento massimo è il massimo valore che voglio dare al corpo per muoversi.
in realtà questo valore non dovrebbe esserci, ma dato che se il punto passa molto
vicino ad un corpo, esso partirebbe in una direzione a v molto elevata.
nella realtà potrebbe anche accadere, ma potrebbe succedere anche che il punto
precipiti sulla superficie della terra.
'''

from turtle import Turtle, Screen
from numpy import *
import math
from decimal import Decimal as dec
import sys

sys.setrecursionlimit(1000000000)

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
        self.altezza=240#da ripicciolire o ingrandire per rimpicciolire o ingrandire il grafico
        self.lunghezza=440
        self.altezza_foraxes=900#quelle per disegnare gli assi
        self.lunghezza_foraxes=1650
        self.contatore=0

        dati=open("dati.txt")
        dati=dati.read()

        dati=dati.split("\n")

        self.raggio_pianeti=int(dati[-2])
        self.s_max=int(dati[-3])

        vyp=int(dati[-5])
        vxp=int(dati[-6])
        yp=int(dati[-7])
        xp=int(dati[-8])

        self.info_punto.append(xp)
        self.info_punto.append(yp)
        self.info_punto.append(vxp)
        self.info_punto.append(vyp)

        for count in range(9):
            dati.pop(-1)

        x=0
        y=0
        massa=0

        for count in range(int((len(dati)/3))):
            [x, y, massa]=[int(dati[0]), int(dati[1]), int(dati[2])]
            self.lista_corpi.append([x, y, massa])
            for i in range(3):
                dati.pop(0)


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
        x_max=(self.lunghezza/2)/abs(self.massimi[0]+0.0000000000000001)
        y_max=(self.altezza/2)/abs(self.massimi[1]+0.0000000000000001)
        self.moltiplicatore_massa=2*self.raggio_pianeti/(self.massimi[2]+0.0000000000000001)

        if x_max>=y_max:
            self.moltiplicatore_coord=y_max
        if x_max<y_max:
            self.moltiplicatore_coord=x_max

        for i in range(2):
            for corpo in self.lista_corpi:
                corpo[i]*=self.moltiplicatore_coord

        for corpo in self.lista_corpi:
            corpo[2]*=self.moltiplicatore_massa

        self.info_punto[0]*=self.moltiplicatore_coord
        self.info_punto[1]*=self.moltiplicatore_coord
        self.info_punto[2]*=self.moltiplicatore_coord
        self.info_punto[3]*=self.moltiplicatore_coord

        print(self.lista_corpi)



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
            self.t.speed(2)
            count+=1


    def disegna_punto(self):
        self.contatore+=1
        if self.contatore>1220:
            self.end_program()
        self.t.goto(round(self.info_punto[0]), round(self.info_punto[1]))
        self.nuovo_punto()

    def continua_traiettoria(self):#condizioni affinche il punto possa continuare Traiettoria

        for corpo in self.lista_corpi:
            if self.info_punto[0]<(corpo[0]+self.raggio_pianeti) and self.info_punto[0]>(corpo[0]-self.raggio_pianeti):
                if self.info_punto[1]<(corpo[1]+self.raggio_pianeti) and self.info_punto[1]>(corpo[1]-self.raggio_pianeti):
                    print('schiantato')
                    self.end_program()

        if self.info_punto[0]<-(self.lunghezza_foraxes*2/3) or self.info_punto[0]>(self.lunghezza_foraxes*2/3) or \
        self.info_punto[1]<-(self.altezza_foraxes*2/3) or self.info_punto[1]>(self.altezza_foraxes*2/3):
            print('corpo si è allontantato troppo')
            self.end_program()

        v_punto=math.sqrt(self.info_punto[2]**2+self.info_punto[3]**2)
        if v_punto>self.s_max:
            print('sparato via')
            self.end_program()
            #se lo spostamento con un solo vettore è maggiore di un tot di pixel (inseriti dall'utente)
            #significa che il punto è passatto molto vicino al corpo e la sua velocità è aumentata troppo
            #quindi o il corpo è passato molto vicino ed ha ripreso velocità, oppure nella realtà si è schiantato sul pianeta

    def end_program(self):
        self.t.up()
        while 1:
            self.t.forward(1)
        return False

    def nuovo_punto(self):
        self.calcola_campi()
        self.calcola_angoli()
        self.calcola_componenti_campi()
        self.calcola_campo_tot()
        self.calcola_angolo_finale()

        self.info_punto[2]+=float(self.componente_campo_x*dec(self.moltiplicatore_coord))
        self.info_punto[3]+=float(self.componente_campo_y*dec(self.moltiplicatore_coord))

        self.continua_traiettoria()

        self.info_punto[0]+=(self.info_punto[2])
        self.info_punto[1]+=(self.info_punto[3])

        print(self.info_punto[0], self.info_punto[1])

        self.t.down()

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
        self.angolo_finale=dec(arctan((float(self.componente_campo_y)+0.0000000000000001)/(float(self.componente_campo_x)+0.0000000000000001)))
        self.angolo_finale=self.angolo_finale*dec(180/math.pi)

Traiettoria()
fine=input('>>> ')
