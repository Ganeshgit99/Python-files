'''
Constructor and desctructor
===========================
1.Constructor is special member function or method that is used to initalize object at the time of creation.
2.It had fixed name as __init__()
3.Automatically called when object is created.

'''
class Student:

    def __init__(self):
        print("Construcotor is called")

    def getdata(self):
        print("GetData is called")

s1=Student()
s2=Student()
s1.getdata()
