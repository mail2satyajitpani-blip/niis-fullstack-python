from abc import*
class Shape(ABC):
	def __init__(self,name):
		self.name=name
		@abstractmethod
		def area(self):
			pass
class Rectangle(Shape):
	def __init__(self,n,l,b):
		super().__init__(n)
		self.length=l
		self.breadth=b
	def area(self):
		return self.length*self.breadth
class Square(Shape):
	def __init__(self,n,l):
		super().__init__(n)
		self.l=l
	def area(self):
		return self.l*self.l
r1=Rectangle("Rectangle",5,7)
print(r1.area())
s1=Square("SQ",4)
print(s1.area())