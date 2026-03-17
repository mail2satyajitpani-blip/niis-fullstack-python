from abc import*
class Demo(ABC):
	@abstractmethod
	def show(self):
		pass
class Demo1(Demo):
	def show(self):
		print("Hi")
d=Demo1()
d.show()