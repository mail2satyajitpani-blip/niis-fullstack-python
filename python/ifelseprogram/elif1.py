print("Enter a number")
no=int(input())
if no<0:
	no=-no
if no<=9:
	print("single digit")
elif no<=99:
	print("double digit")
elif no<=999:
	print("triple digit")
else:
	print("other")