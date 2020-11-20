num=input('num: ')

def find_fraction(num):
    num=round(float(num), 8)
    i=0

    while True:
        i+=1
        for j in range(abs(round(i/num)-1), round(i/num)+1):
            if j!=0:
                if str(round((i/j), 8))==str(float(num)):
                    print(str(i)+'/'+str(j))
                    exit()

find_fraction(num)
