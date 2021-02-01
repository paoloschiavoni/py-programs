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
        self.spostamento_massimo=15#lo spostamento massimo che un punto può fare
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
            self.t.write("m"+str(count)+" ( "+str(corpo[0]/self.moltiplicatore_coord)+", "+str(corpo[1]/self.moltiplicatore_coord)+" )")
            count+=1

        self.calcola_ogni_punto()

    def calcola_ogni_punto(self):
        self.lista_coordinate_punti_x=[]
        self.lista_coordinate_punti_y=[]
        self.separatore=15
        for i in range(round(-self.lunghezza/2), round(self.lunghezza/2), self.separatore):
            self.lista_coordinate_punti_x.append(i)
        for i in range(round(-self.altezza/2), round(self.altezza/2), self.separatore):
            self.lista_coordinate_punti_y.append(i)

        self.punti_per_linea=len(self.lista_coordinate_punti_y)

        '''
        for n in self.lista_coordinate_punti_x:
            self.t.goto(n, round(-self.altezza/2))
            self.t.down()
            self.t.goto(n, round(self.altezza/2))
            self.t.up()
        for k in self.lista_coordinate_punti_y:
            self.t.goto(round(-self.lunghezza/2), k)
            self.t.down()
            self.t.goto(round(self.lunghezza/2), k)
            self.t.up()
        '''

        self.casi_totali=len(self.lista_coordinate_punti_x)*len(self.lista_coordinate_punti_y)

        self.coordinate_punto=[]
        for n in self.lista_coordinate_punti_x:
            for k in self.lista_coordinate_punti_y:
                self.coordinate_punto=[n, k]
                self.calcola_campi()


    def calcola_campi(self):
        self.lista_campi=[]
        for corpo in self.lista_corpi:
            d_quadro=((corpo[0]/(self.moltiplicatore_coord+0.000000001))-(self.coordinate_punto[0]/(self.moltiplicatore_coord+0.000000001)))**2+\
            ((corpo[1]/(self.moltiplicatore_coord+0.000000000000001))-(self.coordinate_punto[1]/(self.moltiplicatore_coord+0.00000000001)))**2
            g=dec((6.67*10**-11)*(corpo[2]/self.moltiplicatore_massa)/d_quadro)
            self.lista_campi.append(g)


        self.calcola_angoli()


    def calcola_angoli(self):
        self.lista_angoli=[]

        for corpo in self.lista_corpi:
            angolo= dec(arctan((corpo[1]-(self.coordinate_punto[1]+0.000000001))/(corpo[0]-(self.coordinate_punto[1]+0.000000001))))#in radianti
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
        self.risultati_finali.append([self.campo_tot, self.angolo_finale, \
        self.componente_campo_x, self.componente_campo_y, self.coordinate_punto])

        '''
        campo_tot           0
        angolo_finale       1
        componente_campo_x  2
        componente_campo_y  3
        coordinate_punto    4
        '''

        if len(self.risultati_finali)>self.casi_totali-1:
            self.campo_max=0
            self.campo_min=1e10000

            for i in self.risultati_finali:
                if i[0]>self.campo_max:
                    self.campo_max=i[0]
                if i[0]<self.campo_min:
                    self.campo_min=i[0]

            for risultato in self.risultati_finali:
                if risultato[0]==self.campo_max:
                    risultato[0]=self.campo_min


            for i in self.risultati_finali:
                if i[0]>self.campo_max:
                    self.campo_max=i[0]


            self.moltiplicatore_campo=dec(self.spostamento_massimo/(self.campo_max/10))

            for risultato in self.risultati_finali:
                risultato[0]*=dec(self.moltiplicatore_campo)
                risultato[2]*=dec(self.moltiplicatore_campo)
                risultato[3]*=dec(self.moltiplicatore_campo)


            self.disegna_vettori()
        #else:
            #print(len(self.risultati_finali), self.casi_totali)


    def disegna_vettori(self):
        self.counter=0
        for risultati in self.risultati_finali:
            self.t.goto(float(risultati[4][0])+float(risultati[2]), float(risultati[4][1])+float(risultati[3]))
            self.t.down()

            self.counter+=1

            if self.counter%self.punti_per_linea==0:
                self.t.up()

'''
            if risultati[2]>0 and risultati[3]>0:

            if risultati[2]<0 and risultati[3]>0:

            if risultati[2]<0 and risultati[3]<0:

            if risultati[2]>0 and risultati[3]<0:
'''




Campo_gravitazionale()
fine=input('>>> ')
