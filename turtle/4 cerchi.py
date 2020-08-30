from turtle import Turtle
t=Turtle()
def cerchio():
    a=0
    while a <=360:
        t.forward(1)
        t.right(1)
        a+=1

t.fillcolor("blue")
t.begin_fill()
for count in range(4):
        print(cerchio())
        t.right(90)
t.end_fill()