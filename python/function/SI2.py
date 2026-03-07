def sical():
	print("Enter principal")
	p=float(input())
	print("Enter rate of interest")
	r=float(input())
	print("Enter time")
	t=float(input())
	si=p*t*r/100
	return si
res=sical()
print("Simple interest=",res)