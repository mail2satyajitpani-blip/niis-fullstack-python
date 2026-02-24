print("Enter salary of emp")
sal=int(input())
if sal>=5000:
	da=sal*(30/100)
	hra=sal*(20/100)
else:
	da=sal*(20/100)
	hra=sal*(10/100)
total=sal+da+hra
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("Total salary=",total)