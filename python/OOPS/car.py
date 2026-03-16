class Car:
	"""docstring for Car"""
	def __init__(self,brand,color):
		self.brand=brand
		self.color=color
		self.speed=0
	def start(self):
		print(self.brand,"car started")
	def accelerate(self):
		self.speed+=20
		print("speed is",self.speed)
	def stop(self):
		self.speed=0
		print("car stopped")
c1=Car("BMW","Blue")
c2=Car("Audi","Red")
c1.start()
c1.accelerate()
c1.stop()
c2.start()
c2.accelerate()
c2.stop()
		