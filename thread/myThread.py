from threading import Thread
class MyThread(Thread):
	
	def __init__(self):
		Thread.__init__(self)
	def run(self):
		print("Sono ", self.getName())
	