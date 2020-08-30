from turtle import Turtle
t= Turtle()
b=int(input("Digita la lunghezza: "))
def spirale(b, t):
    t=Turtle()
    t.fillcolor("light blue")
    a=0
    while True:
        t.forward(b)
        t.right(90)
        a += 1
        spirale (b+1, t)
        if a == 1000:
            break

print(spirale(b, t))