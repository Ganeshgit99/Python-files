'''
Hybrid Inhertiance
-The Inhertiance which is a combination of multiple inhertiance and hierarchical inhertiance is called as Hybrid Inhertiance



                        A
                        |
                ----------------
                |               |
                B               C

                
'''

class A:
    def geta(self):#self=d1
        self.a=int(input("Enter Value:"))
        #d1.a=value

class B:
    def getb(self):#self=d1
        self.b=int(input("Enter Value:"))
        #d1.b=value

class C:
    def getc(self):#self=d1
        self.c=int(input("Enter Value:"))
        #d1.c=value

class D(A,B,C):
    def addition(self):#seld=d1
        t=self.a+self.b+self.c
        #t=d1.a+d1.b+d1.c -- 10+20+30=60
        print("Addition:",t)

d1=D()
d1.geta()#geta(d1)
d1.getb()#getb(d1)
d1.getc()#getc(d1)
d1.addition()#addition(d1)
