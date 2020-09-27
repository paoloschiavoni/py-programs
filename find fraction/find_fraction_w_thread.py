import time
from  threading import Thread

num=input('num: ')
num=round(float(num), 8)

threads=[]

def find_fraction(num, k, start):
	
	for i in range(k*1000, k*1000+1001):
		for j in range(1, 10001):
			if str(round((i/j), 8))==str(float(num)):
				print(str(i)+'/'+str(j))
				finish=time.perf_counter()
				end=input('program finished in '+str(finish-start)+' seconds')

def start():
	start=time.perf_counter()

	for k in range(0, 10):
		t=Thread(target=find_fraction, args=(num, k, start))
		t.daemon=True
		threads.append(t)

	for thread in threads:
		thread.start()
		thread.join()

start()