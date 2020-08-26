"""
Programma che riceve come input il livello e restituisce la curva c 
di quel livello in un'interfaccia grafica turtle
"""

def curvaC(t, x1, y1, x2, y2, livello):
        
    #Se il livello è 1, il programma eseguisce drawLine
    def drawLine(t, x1, y1, x2, y2):
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
    
    if livello==0:
        drawLine(t, x1, y1, x2, y2)
    
    else:
        xm=(x1+x2+y1-y2)//2
        ym=(x2+y1+y2-x1)//2
        curvaC(t, x1, y1, xm, ym, livello-1)
        curvaC(t, xm, ym, x2, y2, livello-1)

def main():
    from turtle import Turtle
    t=Turtle()
    0=t.speed()
    livello=int(input("Digita il livello (maggiore di 0): "))
    t.hideturtle()
    curvaC(t, 200, -200, 200, 200, livello)
    a=input("Digita qualcosa per uscire: ")

main()
