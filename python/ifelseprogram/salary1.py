print("Enter salary of emp")
sal=int(input())
da=sal*(30/100) if sal>=5000 else sal*(20/100)
hra=sal*(20/100) if sal>=5000 else sal*(10/100)
total=sal+da+hra
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("Total salary=",total)