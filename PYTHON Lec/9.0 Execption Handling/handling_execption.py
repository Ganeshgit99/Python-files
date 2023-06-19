'''

handling execption
==================
try....execpt statement is used to handle exception.

try:
    code need to be inspected for exception.
except ExceptionName:
    except block

working of try..except:
=====================
when there is no exception in try block, then try block code is fully executed.

when there is exception in try block,then control moves into except block and execute code in the except block.


'''

a=int(input("Enter Numerator:"))
b=int(input("Enter Denominator:"))
try:
    c=a/b
    print('Division is:',c)
except ZeroDivisionError:
    print("Denominator Cannot be Zero!!")
    




