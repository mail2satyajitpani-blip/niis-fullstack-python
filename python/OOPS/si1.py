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
p = float(input("principal:"))
r = float(input("Rate:"))
t = float(input("Time:"))
i1=SI(p,r,t)
i1.show()
print("Simple interest=",i1.sical())