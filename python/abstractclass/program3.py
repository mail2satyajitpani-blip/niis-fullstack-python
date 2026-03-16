from abc import*
class Shape(ABC):
	def __init__(self,name):
		self.name=name
		@abstractmethod
		def area(self):
			pass
		def perimeter(self):
			pass
class triangle(Shape):
	def __init__(self,n,h,b):
		super().__init__(n)
		self.height=h
		self.base=b
	def area(self):
		return 0.5*self.height*self.base
"""class Square(Shape):
	def __init__(self,n,l):
		super().__init__(n)
		self.l=l
	def area(self):
		return self.l*self.l"""
r1=triangle("Triangle",int(input()),int(input()))
print(r1.area())
