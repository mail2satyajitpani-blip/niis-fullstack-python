print("Enter salary of emp")
sal=int(input())
da,hra=0,0
if sal>=5000:
	da=sal*(30/100)
	hra=sal*(20/100)
total=sal+da+hra
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("Total salary=",total)