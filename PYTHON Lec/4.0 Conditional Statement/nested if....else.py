'''
Need
If there is need to check more than one condition then use nested if...else.

Syntax:
if condition1:
    If
    '''
#Program

n=int(input("Enter Number:"))
if n==0:
    print("Neither negative nor positive")
else:
    if n>0:
        print("Positive Number")
    else:
        print("Negative Number")
        
