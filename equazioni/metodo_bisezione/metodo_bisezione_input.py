equazione=str(input(">>> "))
f=open("metodo_bisezione_compute.py", 'w')

codice= "\
from math import log, sin, cos, tan\n\
def metodo_bisezione():\n\
    #ogni volta che devo calcolare metto x= a quello che devo calcolare\n\
    #controlla se pt in origine\n\
    x=0\n\
    y=FUNCTION \n\
    if y==0:\n\
        print(0.0, 0.0)\n\
        return True\n\
    ax=-1000\n\
    bx=1000\n\
    lim=0.00000000001\n\
    s=10\n\
    x=ax\n\
    ay= FUNCTION \n\
    x=bx\n\
    by= FUNCTION \n\
    #restringe il dominio in caso a o b ne fossero fuori\n\
    if type(ay)==type(pow(-1, 1/2)):\n\
        while True:\n\
            x=ax+s\n\
            y=FUNCTION\n\
            if type(y)==type(pow(-1, 1/2)):\n\
                ax+=s\n\
            if type(y)==type(1.0):\n\
                s/=2\n\
            if s<lim:\n\
                ax+=(2*s)\n\
                break\n\
    if type(by)==type(pow(-1, 1/2)):\n\
        while True:\n\
            x=bx-s\n\
            y=FUNCTION \n\
            if type(y)==type(pow(-1, 1/2)):\n\
                bx-=s\n\
            if type(y)==type(1.0):\n\
                s/=2\n\
            if s<lim:\n\
                bx-=(2*s)\n\
                break\n\
    #vede se monotona crescente o decrescente\n\
    x=ax\n\
    ay= FUNCTION \n\
    x=bx\n\
    by= FUNCTION \n\
    if ay<by:\n\
        c=1\n\
    if ay>by:\n\
        c=-1\n\
    #bisezione\n\
    while True:\n\
        mx=(ax+bx)/2\n\
        x=mx\n\
        my= FUNCTION \n\
        if my > 0:\n\
            if c==1:\n\
                bx=mx\n\
            if c==-1:\n\
                ax=mx\n\
        if my < 0:\n\
            if c==1:\n\
                ax=mx\n\
            if c==-1:\n\
                bx=mx\n\
        if (bx-ax)<lim:\n\
            print(mx, my)\n\
            break\n\
metodo_bisezione()"

codice=codice.replace("FUNCTION", equazione)
f.write(codice)
f.close()
