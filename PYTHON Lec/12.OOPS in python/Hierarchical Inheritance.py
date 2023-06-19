'''
Hierarchical Inhertiance
-The inhertiance in which there are many derived classes and only one base
class is called as Hierarchical Inhertiance.


                        B
                        |
                        |
        ---------------------------------------------
        |       |       |         |       |.........|
        D1      D2      D3        D4      D5        Dn



                        A
                        |
            --------------------------
            |                        |
            B                        C





'''

class A:
    def geta(self):
        self.a=int(input("Enter Value for A:"))

class B(A):
    def getb(self):
        self.b=int(input("Enter Value For B:"))

    def addition(self):
        t1=self.a+self.b
        print("Addtion Of A And B:",t1)
        
class C(A):
    def getc(self):
        self.c=int(input("Enter Value For C:"))

    def addition(self):
        t2=self.a+self.c
        print("Additon of A and C:",t2)

b1=B()
b1.geta()#geta(b1)
b1.getb()#getb(b1)
b1.addition()#addtion(b1)
print()
c1=C()
c1.geta()#geta(c1)
c1.getc()#getc(c1)
c1.addition()#addition(c1)
    
