'''
Need of module:Code reusablity across various pyhton files in project.

With the help of module you can define functionality in one python file and that functionality can be resued in another python file by importiong.


what is module?
-Module is a python file which is a collection of function, constant and classes.

Types of modules
================
1)Built in module.
2)User defined Module.


Built in modules
================
1)math,string,random,datetime.


'''

#import module to use

import math
#n=int(input("Enter Number:"))
r=math.sqrt(16)
print(r)


'''
#aliasing to module
import math as m

'''
'''
#Ceil Vs Floor

15.4=>16 Ceil
15.4=>15 Floor
'''
'''
#Ceil--It Gives you higher value
print(m.ceil(15.4))
print(m.ceil(15.5))
print(m.ceil(15.8))

#Floor--It gives you lower value
print(m.floor(15.4))
print(m.floor(15.5))
print(m.floor(15.8))

#Constant
print("Value of PI is:",m.pi)
print("Value of E is:",m.e)

'''

'''
from math import factorial,sqrt

res=factorial(5)
print("Factorial is:",res)

sq=sqrt(16)
print("Square root:",sq)
'''

#To import all

from math import*
res=factorial(5)
print("Factorial is:",res)

