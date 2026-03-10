class rectangle:
	def __init__(self,l,b):
		self.length=l
		self.breadth=b
	def show(self):
		print("length=",self.length)
		print("breadth=",self.breadth)
	def area(s):
		return s.length*s.breadth
	def perimeter(s):
		print("perimeter=",2*(s.length+s.breadth))
print("Enter rectangle length and breadth")
r1=rectangle(float(input()),float(input()))
r1.show()
print("Area of rectangle=",r1.area())
r1.perimeter()