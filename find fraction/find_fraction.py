import time

num=input('num: ')

def find_fraction(num, start):
    num=round(float(num), 8)
    i=0

    while True:
        i+=1
        for j in range(abs(round(i/num)-1), round(i/num)+1):
            if j!=0:
                if str(round((i/j), 8))==str(float(num)):
                    print(str(i)+'/'+str(j))
                    finish=time.perf_counter()
                    print(f'program finished in {finish-start} seconds')
                    exit()

start=time.perf_counter()
find_fraction(num, start)
finish=time.perf_counter()
print(f'nessuna frazione trovata, \nprogramma finito in {finish-start} secondi')