print("Enter 3 numbers")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
	if no1>=no3:
		print("Biggest no. is",no1)
	else:
		print("Biggest no. is",no3)
else:
	if no2>=no3:
		print("Biggest no. is",no2)
	else:
		print("Biggest no. is",no3)
