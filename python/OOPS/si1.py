class SI:
	def __init__(self,p,r,t):
		self.principal=p
		self.rate=r
		self.time=t
	def show(self):
		print("principal=",self.principal)
		print("Rate of interest=",self.rate)
		print("Time=",self.time)
	def sical(self):
		return self.principal*self.rate*self.time/100
print("Enter principal,rate,time")
p=(float(input())
r=(float(input())
t=(float(input())
	

i1.SI(p,r,t)
print("Simple interest=",i1.sical())