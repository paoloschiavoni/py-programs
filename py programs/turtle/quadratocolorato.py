from turtle import Turtle
import random
t=Turtle()
t.hideturtle()
def drawSquare(t):
    t=Turtle()
    t.screen.bgcolor(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
    lato=int(input("Digita la lunghezza del lato: "))
    t.hideturtle()
    t.up()
    t.goto(-lato/2, lato/2)
    t.setheading(0)
    t.down()
    t.fillcolor(random.uniform(0.0, 1.0), random.uniform(0.0, 1.0), random.uniform(0.0, 1.0))
    t.begin_fill()
    for count in range(4):
        t.forward(lato)
        t.right(90)
    t.end_fill()
    t.up()
    #per non farlo chiudere
    e=int(input(": "))

print(drawSquare(t))