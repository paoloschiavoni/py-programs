import random
import time
lista=[1607, 1620, 1630, 1636, 1776, 1800, 1787, 1756, 1763, 1688, "5 marzo 1770", "16 dicembre 1773", "5 settembre1774", "estate 1776", "4 luglio 1776", "ottobre 1781", 1783]
while len(lista)!=0:
    num=random.choice(lista)
    lista.remove(num)
    print(num)
    time.sleep(10)
