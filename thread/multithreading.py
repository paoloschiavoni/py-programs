import threading
import time

start=time.perf_counter()

'''
def wait():
	print('ready to sleep')
	time.sleep(1)
	print('finish sleeping')
'''

#base
'''
t1=threading.Thread(target=wait)
#non metto le parentesi altrimenti dopo la fa andare subito
#ora la volgio solo creare, per poi farla andare quando voglio

t1.start()
'''

#faccio andare 10 thread, al posto che impiegarci 10 secondi,
#ce ne impiegheranno 1, dato che vanno tutti insieme e sono molto più veloci

threads=[]
'''
for i in range(10):
	t=threading.Thread(target=wait)
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()#serve per farli andare tutti insime
'''

def wait(seconds):
	print(f'ready to sleep {seconds} seconds')
	time.sleep(seconds)
	print('finish sleeping')
for i in range(10):
	t=threading.Thread(target=wait, args=[1.5])#con args posso mettere le variabili
	t.start()
	threads.append(t)
for thread in threads:
	thread.join()

finish=time.perf_counter()
print(f'\n\nfinished in {(finish-start)} seconds')