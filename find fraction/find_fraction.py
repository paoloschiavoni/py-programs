import time

num=input('num: ')
num=round(float(num), 8)

def find_fraction(num, start):

	for i in range(1, 10001):
	    for j in range(1, 10001):
	        if str(round((i/j), 8))==str(float(num)):
	            print(str(i)+'/'+str(j))
	            finish=time.perf_counter()
	            print(f'program finished in {finish-start} seconds')
	            exit()

start=time.perf_counter()
find_fraction(num, start)
finish=time.perf_counter()
print(finish-start)