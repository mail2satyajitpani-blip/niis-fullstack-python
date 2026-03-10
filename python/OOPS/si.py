class SI:
	def __init__(s,p,r,t):
		s.principal=p
		s.rate=r
		s.time=t
	def show(s):
		print("principal=",s.principal)
		print("Rate of interest=",s.rate)
		print("Time=",s.time)
	def sical(s):
		return s.principal*s.rate*s.time/100
i1=SI(10000,7.9,4)
i1.show()
print("Simple interest=",i1.sical())