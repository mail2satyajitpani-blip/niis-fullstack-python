"""wap take two numbers from keyboard enter your choice 1.add 2.sub 3.mult 
invalid choice (menu driven program)"""
print("Enter 2 numbers")
no1=int(input())
no2=int(input())
print("Enter your choice\n1.add 2.sub 3.mult")
ch=int(input())
if ch==1:
	print("SUM=",no1+no2)
elif ch==2:
	print("SUB=",no-no2)
elif ch==3:
	print("mult=",no*no2)
else:
	print("invalid choice")