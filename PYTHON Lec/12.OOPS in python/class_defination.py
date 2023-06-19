'''

Need of OOPS
=============
1.Security
2.User defined Datatype
3.To map real world entity digitally.

OOPS provides following features
1.Abstraction
2.Encapsulation
3.Inheritance
4.Polymorphism

Class and Object are used to implement OOPS.

What is class?
-Class is a blueprint which contains attribute and bheviour [datmembers and methods]

What is Object?
-Object is manufactued from class or it is instance of class that can access class attribute and bheviour.

The process od defining object is called as instantiation.

Data Members
===========
Data members are variable used to store data.

Methods or members function
===========================
These are function defined inside class.


syntax:Class defination

class classname:
        datamembers

        methods


Object
-To access methods and data members of class there is need of object.

syntax:
variable_name=classname()

Accessing method via object.
=========================
objectname.methodname()


'''


class Student:
    def greet(self):
        print("Hello all,Good afternoon!!")

#greet()  ---> NameError: name 'greet' is not defined
    
s1=Student()
s1.greet()

'''
when an object is accessing a method,that object is always passed as an argument to that method.

'''

