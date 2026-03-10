class Student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		print("name=",self.name)
		print("roll=",self.roll)
		print("mark=",self.mark)
s1=Student("Satya",34,90.89)
s2=Student("Damodar",56,56.90)
s1.show()
s2.show()