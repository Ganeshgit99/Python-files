'''
Encapulation
============
1.Biding(wrapping) data members and methods into single unit is called as Encapsulation.

Need
-Security

Real World Ex:
Medicine capsule.

3.Class wrap methods and data member into a single unit,thus class provide security to its data members and methods as they can only access with class object.

Access specifier
====================
1.Public
2.Private

By default all data members and methods had public access specifier.
That is,they can be accessed inside class as well as Outside class.

'''
"""
class Student:
    def display(self):
        print("Name:",self.n)
        print("Roll Number:",self.r)

s1=Student()
s1.n=input("Enter Name:")
s1.r=input("Enter Roll Number:")
s1.display()
"""
class Student:
    def getdata(self):
        s1.n=input("Enter Name:")
        s1.r=input("Enter Roll Number:")
        s1.display()
        
    def display(self):
        print("Name:",self.n)
        print("Roll Number:",self.r)

s1=Student()
s1.getdata()
