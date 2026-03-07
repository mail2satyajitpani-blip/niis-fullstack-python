def fact():
	print("Enter a number")
	no=int(input())
	f=1
	while no>0:
		f=f*no
		no=no-1
print("Factorial=",f)
fact()
