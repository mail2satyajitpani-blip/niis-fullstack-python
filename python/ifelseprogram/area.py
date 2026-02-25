import math
print("choose a shape to calculate area")
print("1.Square\n2.Rectangle\n3.Circle")
choice=int(input("Enter your choice(1-3):"))
if choice ==1:
	side=float(input("Enter sideof the Square "))
	area=side*side
	print("Area=",area)
elif choice==2:
	length=int(input("Enter length of Rectangle"))
	breadth=int(input("Enter breadth of Rectangle"))
	area=length*breadth
	print("area=",area)
elif choice==3:
	radius=int(input("Enter radius of Circle"))
	area=math.pi*radius*radius
	print("Area=",area)
else:
	print("invalid choice")
