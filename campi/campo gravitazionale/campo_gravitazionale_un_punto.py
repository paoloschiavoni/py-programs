from turtle import Turtle
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
        while True:
            try:
                x=int(input("ascissa corpo "+str(len(self.lista_corpi)+1)+": "))
                y=int(input("ordinata corpo "+str(len(self.lista_corpi)+1)+": "))
                massa=int(input("massa corpo "+str(len(self.lista_corpi)+1)+": "))
                print("\n")
                tmp_list=[x, y, massa]
                self.lista_corpi.append(tmp_list)
            except:
                break

        xp=int(input("\nascissa punto: "))
        yp=int(input("ordinata punto: "))
        self.coordinate_punto.append(xp)
        self.coordinate_punto.append(yp)
        self.analizza_corpi()

    def analizza_corpi(self):
        max_x=0
        max_y=0
        max_massa=0
        self.massimi=[max_x, max_y, max_massa]
        for i in range(3):
            for corpo in self.lista_corpi:
                if abs(corpo[i])>abs(self.massimi[i]):
                    self.massimi[i]=abs(corpo[i])

        if self.coordinate_punto[0]>self.massimi[0]:
            self.massimi[0]=self.coordinate_punto[0]
        if self.coordinate_punto[1]>self.massimi[1]:
            self.massimi[1]=self.coordinate_punto[1]

        self.change_coordinates_foraxes()

    def change_coordinates_foraxes(self):
        x_max=(self.lunghezza/2)/self.massimi[0]
        y_max=(self.altezza/2)/self.massimi[1]
        self.moltiplicatore_massa=40/self.massimi[2]
        if x_max>=y_max:
            self.moltiplicatore_coord=y_max
        if x_max<y_max:
            self.moltiplicatore_coord=x_max

        for i in range(2):
            for corpo in self.lista_corpi:
                corpo[i]*=self.moltiplicatore_coord

        for corpo in self.lista_corpi:
            corpo[2]*=self.moltiplicatore_massa

        self.coordinate_punto[0]*=self.moltiplicatore_coord
        self.coordinate_punto[1]*=self.moltiplicatore_coord

        self.disegna_assi()


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
            self.t.dot(corpo[2], "black")
            self.t.goto(corpo[0]+20, corpo[1]+20)
            self.t.write("m"+str(count)+" ( "+str(corpo[0]/(self.moltiplicatore_coord+0.0000000000000001))+", "+str(corpo[1]/(self.moltiplicatore_coord+0.0000000000000001))+" )")
            count+=1

        self.t.up()
        self.t.goto(self.coordinate_punto[0], self.coordinate_punto[1])
        self.t.dot(10, "blue")
        self.t.goto(self.coordinate_punto[0]+20, self.coordinate_punto[1]+20)
        self.t.write("P ( "+str(self.coordinate_punto[0]/(self.moltiplicatore_coord+0.0000000000000001))+", "+str(self.coordinate_punto[1]/(self.moltiplicatore_coord+0.0000000000000001))+" )")

        self.calcola_campi()

    def calcola_campi(self):
        self.lista_campi=[]
        for corpo in self.lista_corpi:
            d_quadro=((corpo[0]/(self.moltiplicatore_coord+0.0000000000000001))-(self.coordinate_punto[0]/(self.moltiplicatore_coord+0.0000000000000001)))**2+\
            ((corpo[1]/(self.moltiplicatore_coord+0.0000000000000001))-(self.coordinate_punto[1]/(self.moltiplicatore_coord+0.0000000000000001)))**2
            g=dec((6.67*10**-11)*(corpo[2]/(self.moltiplicatore_massa+0.0000000000000001))/(d_quadro+0.0000000000000001))
            self.lista_campi.append(g)


        self.calcola_angoli()


    def calcola_angoli(self):
        self.lista_angoli=[]

        for corpo in self.lista_corpi:
            angolo= dec(arctan((corpo[1]-self.coordinate_punto[1])/((corpo[0]-self.coordinate_punto[0])+0.0000000000000001)))#in radianti
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

        self.disegna_vettore()

    def disegna_vettore(self):
        self.t.goto(self.coordinate_punto[0], self.coordinate_punto[1])
        if self.componente_campo_x>0 and self.componente_campo_y>0:
            self.t.seth(float(self.angolo_finale))
            self.t.down()
            self.t.forward(60)
            self.t.seth(float(self.angolo_finale)+float(135))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)-float(45))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)+float(225))
            self.t.forward(10)
            self.t.up()
        if self.componente_campo_x<0 and self.componente_campo_y>0:
            self.t.seth(float(180)+float(self.angolo_finale))
            self.t.down()
            self.t.forward(60)
            self.t.seth(float(self.angolo_finale)+float(315))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)+float(135))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)+float(45))
            self.t.forward(10)
            self.t.up()
        if self.componente_campo_x<0 and self.componente_campo_y<0:
            self.t.seth(float(180)+float(self.angolo_finale))
            self.t.down()
            self.t.forward(60)
            self.t.seth(float(self.angolo_finale)+float(315))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)+float(135))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)+float(45))
            self.t.forward(10)
            self.t.up()
        if self.componente_campo_x>0 and self.componente_campo_y<0:
            self.t.seth(float(self.angolo_finale))
            self.t.down()
            self.t.forward(60)
            self.t.seth(float(self.angolo_finale)-float(135))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)+float(45))
            self.t.forward(10)
            self.t.seth(float(self.angolo_finale)-float(225))
            self.t.forward(10)
            self.t.up()

        print("\ncomponente x:", self.componente_campo_x)
        print("componente y:", self.componente_campo_y)
        print("angolo:", round(self.angolo_finale))
        print("modulo campo finale:", self.campo_tot)

Campo_gravitazionale()
fine=input('>>> ')
