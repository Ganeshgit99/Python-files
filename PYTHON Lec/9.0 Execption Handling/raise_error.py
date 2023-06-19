'''
raising exception
==================
Exception can be raised by keyword saise

syntax:
    raise ExceptionName('Error Message')

ExceptionName is built in Exception.
e.g ZeroDivisionError,ValueError,ModuleNotFoundError etc

'''

a=int(input("Enter Numerator:"))
b=int(input("Enter Denominator:"))
if b!=0:
    c=a/b
    print("Division is:",c)
else:
 raise ZeroDivisionError("Denominator Cannot be zero")
