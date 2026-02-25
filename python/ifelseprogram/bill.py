print("Enter total electricity consumed")
units=int(input())
bill=0
if units<=100:
	bill=units*1.5
elif units<=200:
	bill=(100*1.5)+(units-100)*2.5
elif units<=300:
	bill=(100*1.5)+(100*2.5)+(units-200)*4.0
else:
	bill=(100*1.5)+(100*2.5)+(100*3.5)+(units-300)*6.0
print("Total bill=",bill)