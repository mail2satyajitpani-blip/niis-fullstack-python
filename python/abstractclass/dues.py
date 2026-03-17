from abc import *
class Dues(ABC):
	@abstractmethod
	def coursefee(self,fee):
		pass
	def hostelfee(self,fee):
		pass
class Student(Dues):
	def coursefee(self,fee):
		return fee
	def hostelfee(self,fee):
		return fee
s=Student()
print("Coursefee:",s.coursefee(100000))
print("Hostelfee" ,s.hostelfee(60000))