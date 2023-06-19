'''
try with multiple except to handle more than one exception.

syntax:
try:
    code to be inspected

except ExceptionName1:
    code
except ExceptionName2:
    code
.
.
except ExceptionNamen:
    code

'''
'''
try:
    a=int(input("Enter Numerator:"))
    b=int(input("Enter Denominator:"))
    c=a/b
    print('Division is:',c)
except ZeroDivisionError:
    print("Denominator Cannot be Zero!!")
except ValueError:
    print("Inputs must be a number or digit")

'''
'''
try:
    a=int(input("Enter Numerator:"))
    b=int(input("Enter Denominator:"))
    c=a/b
    print('Division is:',c)
except Exception as e:
    print("Error:",e)
    '''

