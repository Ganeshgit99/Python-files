'''
Single Inhertiance

The inhertiance that had one baase class and one derived class is called as single Inhertiance.

        A
        |
        |
        |
        B

'''

class A:
    def geta(self):
        self.a=int(input("Enter Value of A:"))

class B(A):
        def getb(self):
            self.b=int(input("Enter Value of B:"))

        def addition(self):
            t=self.a+self.b
            print("Addition is:",t)


b1=B()
b1.geta()
b1.getb()
b1.addition()
