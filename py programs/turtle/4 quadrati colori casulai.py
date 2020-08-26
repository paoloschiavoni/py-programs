
"""disegna 4 quadrati negli angoli, uno nero, uno grigio e due colori casuali"""

from turtle import Turtle
import random


def drawSquare(t, x, y, lato):
    """Disegna quadrato dallangolo superiore sinistro"""
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for count in range(4):
        t.forward(lato)
        t.left(90)


def main():
    t=Turtle()   
    """lunghezza lato"""
    lunghezza=40
    """Trova la lunghezza della metà della lunghezza dello schermo
    e della metà della sua altezza"""
    altezza=t.screen.window_width() //4
    larghezza=t.screen.window_height()//4
    """inizia a disegnare nellangolo sinistro in alto"""
    drawSquare(t, -larghezza, altezza, lunghezza)
    """disegna quadrato in alto a destra grigio"""
    t.pencolor(0.5, 0.5, 0.5)
    drawSquare(t, larghezza-lunghezza, altezza, lunghezza)
    """primo colore casuale,basso a sinistra"""
    t.pencolor(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
    drawSquare(t, - larghezza, lunghezza- altezza, lunghezza)
    """secondo colore casuale in basso a destra"""
    t.pencolor(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
    drawSquare(t, larghezza-lunghezza, lunghezza-altezza, lunghezza)





main()