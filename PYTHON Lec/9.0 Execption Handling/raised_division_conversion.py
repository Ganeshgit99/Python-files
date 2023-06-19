'''
checking for digit and denominator Zero.

'''

a=input("Enter Numerator:")
b=input("Enter Denominator:")
if a.isdigit() and b.isdigit():
    x=int(a)
    y=int(b)
    if y!=0:
      z=x/y
      print("Division is:",z)
    else:
        raise ZeroDivisionError("Dernominator Cannot b]e Zero")
else:
    raise ValueError("Please Enter Digit or Number")
