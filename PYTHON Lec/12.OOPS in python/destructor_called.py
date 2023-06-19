"""
Destructor
==========
1.It is special method used to release memory space allocated to object.
2.Ir had fixed name as __del__().
3.It is called automatically when program ends.

"""

class Student:
    def __init__(self):
        print("Constructor Is called...")

    def __del__(self):
        print("Destructor is called...")
        
s1=Student() #constructor is called
s2=Student() #constructor is called
