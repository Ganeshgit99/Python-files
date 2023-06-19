'''
Multiple Inhertiance
-The inhertiance in which there are many base classes and only one dervied
classes is called as Multiple Inhertiance.


            B1      B2      B3 ....... Bn
            |       |       |           |
            -----------------------------
                         |
                         |
                         D


                    A        D
                    |        |
                    ----------
                        |
                        C

Deived Class Syntax:

Class D(B1,B2,B3,....,Bn):

     body

'''

class A:
    def geta(self):#self=c1
        self.a=int(input("Enter Value of A:"))
       #c1.a=value
class B:
    def getb(self):#self=c1
        self.b=int(input("Enter Value Of B:"))
       #c1.b=value
class C(A,B):
    def addtion(self):#self=c1
        t=self.a+self.b
        #t=c1.a+c1.2=result----->10+20=30
        print("Addition is:",t)

c1=C()
c1.geta()#geta(c1)
c1.getb()#getb(c1)
c1.addtion()#addtion(c1)

