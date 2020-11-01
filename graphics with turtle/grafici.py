from turtle import Turtle
import math
from math import *
from find_fr_to_import import find_fraction

class Grafico(Turtle):
    def __init__(self):

        Turtle.__init__(self)
        Turtle.hideturtle(self)#per farla comparire all'inizio invisibile
        self.t=Turtle()
        self.t.hideturtle()
        self.t.speed(0)
        self.contatore=0#serve per la scrittura della funzione
        self.equazione=''


        self.altezza=800
        self.lunghezza=1550

        print('\nL\'equazione deve essere scritta con degli spazi \nche separano i vari elementi dopo di essi, ad esempio:\n\n\
proporzionalità diretta: y= ax +b\n\
retta parallela all\'asse x: y= a\n\
proporzionalità inversa: y= a/x\n\
proporzionalità quadratica: y= ax**2 +bx +c\n\
proporzionalità cubica: y= ax**3 +b\n\
radicale: y= ardc( bx +c) +d\n\
modulo: y= amdl( bx +c) +d\n\n')

        self.disegna_assi()
        self.calcolatrice()
        self.analizza_equazione()

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

    def calcolatrice(self):
        calcolo=str(input("Nel caso ti servisse fare dei conti (non usare frazioni nell'equazione):\nPrememre invio per continuare\n>>> "))
        lista_calcolo=[]
        if calcolo =='':
            self.scrivi_equazione()
        else:
            lista_calcolo=calcolo.split(" ")
            a=int(lista_calcolo[0])
            b=int(lista_calcolo[2])
            operazione=lista_calcolo[1]
            if operazione=="+":
                print(a+b)
            elif operazione=="-":
                print(a-b)
            elif operazione=="*":
                print(a*b)
            elif operazione=='/':
                print(a/b)
            self.scrivi_equazione()

    def scrivi_equazione(self):
        self.equazione=str(input("\nDigita l'equazione ordinata, \nse un coefficiente o un termine noto dovesse essere 0 o 1, specificarlo\nInizia con y= ...\n>>>"))
        self.t.up()
        self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -30)
        self.t.write(self.equazione, font=("Calibri", 20))

    def analizza_equazione(self):
        self.lista_membri_eq=self.equazione.split(" ")
        membro = self.lista_membri_eq[1]
        if "x**3" in membro:
            print('\nproporzionalità cubica\n')
            self.analizza_cubica()
        if "x**2" in membro:
            print('\nproporzionalità quadratica\n')
            self.analizza_quadratica()
        if not "x**3" in membro and not "x**2" in membro and "x" in membro and not '/' in membro and not 'rdc(' in membro and not 'mdl(' in membro:
            print('\nproporzionalità diretta\n')
            self.analizza_retta()
        if not "x**3" in membro and not "x**2" in membro and not 'x' in membro and not '/' in membro and not 'rdc(' in membro and not 'mdl(' in membro:
            print('\nparallela ad x\n')
            self.analizza_parallelax()
        if '/' in membro and not 'x**' in membro and not 'rdc(' in membro:
            print('\nproporzionalità inversa\n')
            self.analizza_inversa()
        if 'rdc(' in membro:
            print('\ngrafico di una radice\n')
            self.analizza_radice()
        if 'mdl(' in membro:
            print('\ngrafico con modulo\n')
            self.analizza_modulo()

    def analizza_cubica(self):
        self.lista_coeff=[]

        for membro in self.lista_membri_eq:
            if 'x**3' in membro:
                for el in membro:
                    self.lista_coeff.append(el)
                for count in range(4):
                    self.lista_coeff.pop()
                self.coeff=float(''.join(self.lista_coeff))

            if not 'x' in membro and not 'y=' in membro:
                self.tnoto=float(membro)
        if self.coeff==0:
            print('Errore: il coefficiente dell\'x**3 non deve essere 0,\naltrimenti si ottiene il grafico di una retta parallela all\'asse x\n')
        if self.coeff!=0:
            self.disegna_cubica()

    def disegna_cubica(self):
        self.y=-self.altezza/2
        self.x=self.radice_cubica((self.y-self.tnoto)/self.coeff)

        while self.y<self.altezza/2:
            self.y=(self.coeff*(self.x**3))+self.tnoto
            self.t.goto(self.x, self.y)
            self.t.down()
            self.x+=1

        self.t.up()
        self.punti_int_cubica()

    def punti_int_cubica(self):
        self.int_x=self.radice_cubica(-self.tnoto/self.coeff)
        self.int_x=find_fraction(self.int_x)
        self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
        self.t.write('Il punto di intersezione con l\'asse x è: ', font=('Calibri', 17))
        self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
        self.t.write('('+str(self.int_x)+', 0.0)', font=('Calibri', 17))
        self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -140)
        self.t.write('Il punto di intersezione con l\'asse y è: ', font=('Calibri', 17))
        self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
        self.tnoto=find_fraction(self.tnoto)
        self.t.write('(0.0, '+str(self.tnoto)+')', font=('Calibri', 17))

    def radice_cubica(self, x):
        if x>0:
            return math.pow(x, float(1)/3)
        if x<0:
            return -math.pow(abs(x), float(1)/3)
        if x==0:
            return 0

    def analizza_quadratica(self):
        self.lista_coeff2=[]
        self.lista_coeff1=[]

        for membro in self.lista_membri_eq:

            if 'x**2' in membro:
                for el in membro:
                    self.lista_coeff2.append(el)
                for count in range(4):
                    self.lista_coeff2.pop()
                self.coeff2=float(''.join(self.lista_coeff2))

            if 'x' in membro and not '*' in membro:
                for el in membro:
                    self.lista_coeff1.append(el)
                self.lista_coeff1.remove('x')
                self.coeff1=float(''.join(self.lista_coeff1))

            if not 'x' in membro and not 'y=' in membro:
                self.tnoto=float(membro)

        if self.coeff2==0:
            print('Errore: il coefficiente dell\'x**2 non deve essere 0,\naltrimenti si ottiene il grafico di una retta\n')

        if self.coeff2!=0:
            self.disegna_quadratica()

    def disegna_quadratica(self):
        self.x=0
        self.y=0

        for i in range(round(-self.lunghezza/2), round(self.lunghezza/2)):
            self.x=i
            self.y=(self.coeff2*(self.x**2))+(self.coeff1*self.x)+self.tnoto
            self.t.goto(self.x, self.y)
            self.t.down()

        self.t.up()
        self.determinante=(self.coeff1**2)-(4*self.coeff2*self.tnoto)
        self.punti_int_quadratica()

    def punti_int_quadratica(self):
        if self.determinante==0:
            self.soluzione=-self.coeff1/(2*self.coeff2)
            self.soluzione=find_fraction(self.soluzione)
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('Il punto di intersezione con l\'asse x è: ', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.t.write('('+str(self.soluzione)+', 0.0)', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -140)
            self.t.write('Il punto di intersezione con l\'asse y è: ', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
            self.tnoto=find_fraction(self.tnoto)
            self.t.write('(0.0, '+str(self.tnoto)+')', font=('Calibri', 17))

        if self.determinante>0:
            self.soluzione1=(-self.coeff1 + math.sqrt(self.determinante))/(2*self.coeff2)
            self.soluzione2=(-self.coeff1 - math.sqrt(self.determinante))/(2*self.coeff2)
            self.soluzione1=find_fraction(self.soluzione1)
            self.soluzione2=find_fraction(self.soluzione2)

            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('I punti di intersezione con l\'asse x sono: ', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.t.write('('+str(self.soluzione1)+', 0.0)', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -130)
            self.t.write('('+str(self.soluzione2)+', 0.0)', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
            self.t.write('Il punto di intersezione con \'asse y è: ', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -200)
            self.tnoto=find_fraction(self.tnoto)
            self.t.write('(0.0, '+str(self.tnoto)+')', font=('Calibri', 17))

        if self.determinante<0:
            self.tnoto=find_fraction(self.tnoto)
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('Il punto di intersezione con \'asse y è: ', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.t.write('(0.0, '+str(self.tnoto)+')', font=('Calibri', 17))


    def analizza_retta(self):
        self.lista_coeff=[]

        for membro in self.lista_membri_eq:
            if "x" in membro:
                for el in membro:
                    self.lista_coeff.append(el)
                self.lista_coeff.remove('x')
                self.coeff=float("".join(self.lista_coeff))

            if not "x" in membro and not "y" in membro:
                self.tnoto=float(membro)

        if self.coeff==0:
            print('Errore: il coefficiente dell\'x non deve essere 0,\naltrimenti si ottiene il grafico di una retta parallela all\'asse x\n')
        if self.coeff!=0:
            self.disegna_retta()


    def disegna_retta(self):
        self.x=0
        self.y=0

        self.i=-self.altezza/2#serve per la posizione della freccia
        while self.i<self.altezza/2:
            self.y=self.i
            self.x=(self.y-self.tnoto)/self.coeff
            self.t.goto(self.x, self.y)
            self.t.down()
            self.i+=3

        self.t.up()
        self.punti_int_retta()

    def punti_int_retta(self):
        if self.tnoto==0:
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('L\'unico punto di intersezione con gli assi è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.t.write('(0.0, 0.0)', font=('Calibri', 17))
        if self.tnoto!=0 and self.coeff!=0:
            self.intersezione_x=-self.tnoto/self.coeff
            self.intersezione_x=find_fraction(self.intersezione_x)
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('Il punto di intersezione con l\'asse x è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.t.write('('+str(self.intersezione_x)+', 0.0)', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -140)
            self.t.write('Il punto di intersezione con l\'asse y è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
            self.tnoto=find_fraction(self.tnoto)
            self.t.write('(0.0, '+str(self.tnoto)+')', font=('Calibri', 17))


    def analizza_parallelax(self):
        for membro in self.lista_membri_eq:
            if not 'y=' in membro:
                self.tnoto=float(membro)
        self.disegna_parallelax()

    def disegna_parallelax(self):
        self.x_iniziale=round(-self.lunghezza/2)
        self.x_finale=round(self.lunghezza/2)

        self.t.goto(self.x_iniziale, self.tnoto)
        self.t.down()
        self.t.goto(self.x_finale, self.tnoto)
        self.t.up()
        self.punti_int_parallelax()

    def punti_int_parallelax(self):
        if self.tnoto==0:
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('I punti di intersezione con l\'asse x sono:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.t.write('Per ogni x appartenente ad R', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -140)
            self.t.write('Il punto di intersezione con l\'asse y è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
            self.t.write('(0.0, '+str(self.tnoto)+')', font=('Calibri', 17))
        if self.tnoto!=0:
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('Il punto di intersezione con l\'asse y è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.tnoto=find_fraction(self.tnoto)
            self.t.write('(0.0, '+str(self.tnoto)+')', font=('Calibri', 17))

    def analizza_inversa(self):
        self.lista_coeff=[]

        for membro in self.lista_membri_eq:
            if '/' in membro:
                for el in membro:
                    self.lista_coeff.append(el)
                self.lista_coeff.remove('x')
                self.lista_coeff.remove('/')
                self.num=float(''.join(self.lista_coeff))

        if self.num==0:
            print('Errore: il numeratore non deve essere 0,\naltrimenti si ottiene il grafico di una retta parallela all\'asse x\n')
        if self.num!=0:
            self.disegna_inversa()

    def disegna_inversa(self):

        for i in range(round(-self.altezza/2), -1):
            self.y=i
            self.x=self.num/self.y

            self.t.goto(self.x, self.y)
            self.t.down()

        self.t.up()

        for i in range(1, round(self.altezza/2)):
            self.y=i
            self.x=self.num/self.y

            self.t.goto(self.x, self.y)
            self.t.down()
        self.t.up()
        self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
        self.t.write('Non ci sono punti di intersezione con gli assi', font=('Calibri', 17))



    def analizza_radice(self):#è del tipo a*rdc(bx +c) +d
        self.lista_a=[]
        self.lista_b=[]
        self.lista_c=[]

        for membro in self.lista_membri_eq:
            if 'rdc(' in membro:
                for el in membro:
                    self.lista_a.append(el)
                self.lista_a.remove('r')
                self.lista_a.remove('d')
                self.lista_a.remove('c')
                self.lista_a.remove('(')

                self.a=float(''.join(self.lista_a))

            if 'x' in membro:
                for el in membro:
                    self.lista_b.append(el)
                self.lista_b.remove('x')

                self.b=float(''.join(self.lista_b))

            if ')' in membro:
                for el in membro:
                    self.lista_c.append(el)
                self.lista_c.remove(')')

                self.c=float(''.join(self.lista_c))

            if not 'rdc(' in membro and not ')' in membro and not 'y' in membro and not 'x' in membro:
                self.tnoto=float(membro)

        if self.a==0:
            print('Errore: il coefficiente della radice non deve essere 0,\naltrimenti si ottiene il grafico di una retta parallela all\'asse x\n')

        if self.b==0:
            print('Errore: il coefficiente della x non deve essere 0,\naltrimenti si ottiene il grafico di una retta parallela all\'asse x\n')

        if self.a !=0 and self.b!=0:
            self.disegna_radice()

    def disegna_radice(self):
        self.x=1000000000000
        self.y=0

        for i in range(round(-self.altezza/2 -50), round(self.altezza/2 +50)):
            self.y=i
            self.x=round(((((self.y-self.tnoto)/self.a)**2)-self.c)/self.b)
            if (self.x*self.b + self.c)>=0 and ((self.y-self.tnoto)/self.a)>=0:
                self.t.goto(self.x, self.y)
                self.t.down()
        self.t.up()
        self.punti_int_radice()

    def punti_int_radice(self):
        if -self.tnoto/self.a>=0:
            self.int_x=(((self.tnoto/self.a)**2)-self.c)/self.b

            if self.int_x*self.b + self.c>=0:
                self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
                self.t.write('Il punto di intersezione con l\'asse x è:', font=('Calibri', 17))
                self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
                self.int_x=find_fraction(self.int_x)
                self.t.write('('+str(self.int_x)+', 0.0)', font=('Calibri', 17))

            elif self.int_x*self.b + self.c<0:
                self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
                self.t.write('Non ci sono punti di intersezione con l\'asse x', font=('Calibri', 17))

        if -self.tnoto/self.a<0:
                self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
                self.t.write('Non ci sono punti di intersezione con l\'asse x', font=('Calibri', 17))

        if self.c>=0:
            self.int_y=self.a*math.sqrt(self.c)+self.tnoto
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -140)
            self.t.write('Il punto di intersezione con l\'asse y è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
            self.int_y=find_fraction(self.int_y)
            self.t.write('(0.0, '+str(self.int_y)+')', font=('Calibri', 17))
        if self.c<0:
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -140)
            self.t.write('Non ci sono punti di intersezione con l\'asse y', font=('Calibri', 17))


    def analizza_modulo(self):
        self.lista_a=[]
        self.lista_b=[]
        self.lista_c=[]

        for membro in self.lista_membri_eq:
            if 'mdl(' in membro:
                for el in membro:
                    self.lista_a.append(el)
                self.lista_a.remove('m')
                self.lista_a.remove('d')
                self.lista_a.remove('l')
                self.lista_a.remove('(')
                self.a=float(''.join(self.lista_a))

            if 'x' in membro:
                for el in membro:
                    self.lista_b.append(el)
                self.lista_b.remove('x')
                self.b=float(''.join(self.lista_b))

            if ')' in membro:
                for el in membro:
                    self.lista_c.append(el)
                self.lista_c.remove(')')
                self.c=float(''.join(self.lista_c))

            if not ')' in membro and not 'mdl(' in membro and not 'y=' in membro and not 'x' in membro:
                self.tnoto=float(membro)

        if self.a==0:
            print('Errore: il coefficiente del modulo non deve essere 0,\naltrimenti si ottiene il grafico di una retta parallela all\'asse x\n')

        if self.b==0:
            print('Errore: il coefficiente della x non deve essere 0,\naltrimenti si ottiene il grafico di una retta parallela all\'asse x\n')

        if self.a !=0 and self.b!=0:
            self.disegna_modulo()

    def disegna_modulo(self):
        for i in range(round(-self.lunghezza/2), round(self.lunghezza/2), 10):
            self.x=i
            self.y=self.a*abs((self.x*self.b)+self.c)+ self.tnoto

            self.t.goto(self.x, self.y)
            self.t.down()
        self.t.up()
        self.punti_int_modulo()

    def punti_int_modulo(self):

        self.int_y=self.a*abs(self.c)+self.tnoto

        if -self.tnoto/self.a>0 and self.b!=0:#ha punti di intersezione con x
            self.soluzione1=((self.tnoto/self.a)-self.c)/self.b
            self.soluzione2=((-self.tnoto/self.a)-self.c)/self.b

            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('I punti di intersezione con l\'asse x sono:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.soluzione1=find_fraction(self.soluzione1)
            self.t.write('('+str(self.soluzione1)+', 0.0)', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -130)
            self.soluzione2=find_fraction(self.soluzione2)
            self.t.write('('+str(self.soluzione2)+', 0.0)', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
            self.t.write('Il punto di intersezione con l\'asse y è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -200)
            self.int_y=find_fraction(self.int_y)
            self.t.write('(0.0, '+str(self.int_y)+')', font=('Calibri', 17))

        if self.tnoto==0 and self.a!=0 and self.b!=0:
            self.soluzione=-self.c/self.b

            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('Il punto di intersezione con l\'asse x è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.soluzione=find_fraction(self.solzione)
            self.t.write('('+str(self.soluzione)+', 0.0)', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -140)
            self.t.write('Il punto di intersezione con l\'asse y è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -170)
            self.int_y=find_fraction(self.int_y)
            self.t.write('(0.0, '+str(self.int_y)+')', font=('Calibri', 17))

        if -self.tnoto/self.a<0:
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -70)
            self.t.write('Il punto di intersezione con l\'asse y è:', font=('Calibri', 17))
            self.t.goto(-self.lunghezza/2 +20, self.altezza/2 -100)
            self.int_y=find_fraction(self.int_y)
            self.t.write('(0.0, '+str(self.int_y)+')', font=('Calibri', 17))

Grafico()
fine=input('>>> ')
