from turtle import Turtle
t=Turtle()
import random

def randomWalk(t, volte, distanza):
    import random
    for count in range(volte):
        giro=random.randint(1, 360)
        t.forward(distanza)
        t.left(giro)
    t.hideturtle()


print(randomWalk(Turtle(), volte=random.randint(10, 30), distanza=random.randint(20, 50)))