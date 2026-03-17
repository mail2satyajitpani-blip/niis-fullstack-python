from abc import *
class Student(ABC):

    @abstractmethod
    def show(self):
        pass
class CollegeStudent(Student):
    def show(self):
        print("This is a college student")
s = CollegeStudent()
s.show()