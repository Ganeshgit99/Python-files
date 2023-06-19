'''
methods and data member
====================
'''

class Student:
    def getdata(self):#self=s1,self=s2
        self.n=input("Enter Student Name:")
        #s1.n="Itvedant",s2.n="Pune"
        self.r=input("Enter Roll No:")
        #s1.r=35,s2.r=40

    def display(self):#self=s1,self=s2
        print("Student Name:",self.n)#s1.n="Itvedant",s2.n="Pune"
        print("Roll No:",self.r)#s1.r=35,s2.r=40

s1=Student()
s2=Student()
s1.getdata()
s2.getdata()
print()
print("Information is:")
s1.display()#display(s1)
s2  .display()#display(s2)
