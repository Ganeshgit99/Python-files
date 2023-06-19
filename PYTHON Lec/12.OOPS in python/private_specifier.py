'''
private access specifier
======================
When data members and methods are defined to be private,
they can only accessed inside class they cannot be accessed outside
class.

syntax private data members:
===========================
__variablename

private method
==============
__methodname()

private datamembers and Methods begins with double underscore.

'''
'''
class Student:
    def getdata(self):
        self.__n=input("Enter Name:")
        self.__r=input("Enter Roll Number:")

s1=Student()
s1.getdata()
print("Name:".s1.__n)#Error
print("Roll Number:",s1.__r)#Error
'''

class Student:
    def __getdata(self):
        self.__n=input("Enter Name:")
        self.__r=input("Enter Roll Number:")

    def display(self):
        self.__getdata()
        print("Name:",self.__n)
        print("Roll Number",self.__r)

s1=Student()
s1.display()
s1=Student()

