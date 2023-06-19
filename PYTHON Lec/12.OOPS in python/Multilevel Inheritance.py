'''
Multilevel Inheritance

        A BAse Class
        |
        |
        B Intermediate base
        |
        |
        C Intermediate base
        |
        |
        D Derived Class
'''

class A:
    def geta(self):#self=d1-->geta(d1)
        self.a=int(input("Enter Value For A:"))
        #d1.a=value
class B(A):
    def getb(self):#self=d1-->getb(d1)
        self.b=int(input("Enter Value For B:"))
       #d1.b=value
class C(B):
    def getc(self):#self=d1-->getc(d1)
        self.c=int(input("Enter Value For C:"))
       #d1.c=value
class D(C):
    def addition(self):#self=d1-->additon(d1)
        t=self.a+self.b+self.c
        print("Addition is:",t)

d1=D()
d1.geta()
d1.getb()
d1.getc()
d1.addition()
