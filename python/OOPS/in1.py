class Person:
    def f1(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
class Student:
    def f2(self):
        self.roll_no = int(input("Enter roll number: "))
class EngineeringStudent(Person, Student):
    def get_engineering_data(self):
        self.branch = input("Enter branch: ")
    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Branch:", self.branch)
e = EngineeringStudent()
e.f1()
e.f2()
e.get_engineering_data()
e.display()