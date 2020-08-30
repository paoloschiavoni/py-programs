x=float(input("digitare il numero di cui si vuole trovare la radice: "))
z=1
import math
print(math.sqrt(x))
while True:
    z = (z+(x/z))/2
    if z**2 == x:
        break
print(z)
