from math import log, sin, cos, tan
def metodo_bisezione():
    #ogni volta che devo calcolare metto x= a quello che devo calcolare
    #controlla se pt in origine
    x=0
    y=pow(x, 3)-5
    if y==0:
        print(0.0, 0.0)
        return True
    ax=-1000
    bx=1000
    lim=0.00000000001
    s=10
    x=ax
    ay= pow(x, 3)-5
    x=bx
    by= pow(x, 3)-5
    #restringe il dominio in caso a o b ne fossero fuori
    if type(ay)==type(pow(-1, 1/2)):
        while True:
            x=ax+s
            y=pow(x, 3)-5
            if type(y)==type(pow(-1, 1/2)):
                ax+=s
            if type(y)==type(1.0):
                s/=2
            if s<lim:
                ax+=(2*s)
                break
    if type(by)==type(pow(-1, 1/2)):
        while True:
            x=bx-s
            y=pow(x, 3)-5
            if type(y)==type(pow(-1, 1/2)):
                bx-=s
            if type(y)==type(1.0):
                s/=2
            if s<lim:
                bx-=(2*s)
                break
    #vede se monotona crescente o decrescente
    x=ax
    ay= pow(x, 3)-5
    x=bx
    by= pow(x, 3)-5
    if ay<by:
        c=1
    if ay>by:
        c=-1
    #bisezione
    while True:
        mx=(ax+bx)/2
        x=mx
        my= pow(x, 3)-5
        if my > 0:
            if c==1:
                bx=mx
            if c==-1:
                ax=mx
        if my < 0:
            if c==1:
                ax=mx
            if c==-1:
                bx=mx
        if (bx-ax)<lim:
            print(mx, my)
            break
metodo_bisezione()
