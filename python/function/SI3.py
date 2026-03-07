def sical(p,t,r):
	si=p*t*r/100
	return si
print("Enter principal")
p=float(input())
print("Enter rate of interest")
r=float(input())
print("Enter time")
t=float(input())
res=sical(p,t,r)
print("si=",res)