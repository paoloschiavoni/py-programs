from threading import Thread, currentThread
import random, time

def main():
    #riceve un numero di processi dall'utente
    #avvia un produtore e consumatore
    numAccess=int(input("Digita il numero di accessi: "))

    sleepMax=2
    cell=ShareCell()
    producer=Producer(cell, numAccess, sleepMax)
    consumer=Consumer(cell, numAccess, sleepMax)
    print("Starting the threads")
    producer.start()
    time.sleep(1)
    consumer.start()

class ShareCell(object):

    def __init__(self):
        self.data=-1

    def setData(self, data):
        #del produttore per modificare i dati
        print(currentThread().getName(), "setting data to", data)
        self.data=data

    def getData(self):
        #del consumatore per accedere ai dati
        print(currentThread().getName(), "accessing data to ", self.data)
        return self.data

class Producer(Thread):
    def __init__(self, cell, numAccess, sleepMax):
        Thread.__init__(self, name="Producer")
        self.cell=cell
        self.numAccess=numAccess
        self.sleepMax=sleepMax

    def run(self):
        print(self.getName(), "starting up")
        for count in range(self.numAccess):
            time.sleep(self.sleepMax)
            self.cell.setData(count+1)
        print(self.getName(), "is done producing")

class Consumer(Thread):
    def __init__(self, cell, numAccess, sleepMax):
        Thread.__init__(self, name="Consumer")
        self.cell=cell
        self.numAccess=numAccess
        self.sleepMax=sleepMax

    def run(self):
        print(self.getName(), "starting up")
        for count in range(self.numAccess):
            time.sleep(self.sleepMax)
            value=self.cell.getData()
        print(self.getName(), "is done consuming")
main()
