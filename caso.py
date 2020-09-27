num=input('num: ')
num=round(float(num), 8)
i=1.0
j=1.0
counter=0

def find_fraction(num, i, j, counter):
    while True:
        if str(round((i/j), 8))==str(float(num)):
            print(str(i)+'/'+str(j))
            break
        if counter%2==0:
            i+=1
        if counter%2==1:
            j+=1
        counter+=1

find_fraction(num, i, j, counter)