class Customer:
    def __init__(self):
        self.bname="SBI"
        self.branch="FC ROAD"
        self.ifsc="SBIN23456"
    def getdetails(self):
        self.cname=input("Enter Customer Name:")
        self.mob=input("Mobile Number:")

    def display(self):
        print()
        print("Customer Information:")
        print()
        print("Bank Name:",self.bname)
        print("Branch:",self.branch)
        print("IFSC:",self.ifsc)
        print("Customer Name:",self.cname)
        print("Mobile Number",self.mob)

c1=Customer()
c1.getdetails()
c1.display()
