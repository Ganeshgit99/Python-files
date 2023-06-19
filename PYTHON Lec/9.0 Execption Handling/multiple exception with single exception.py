'''

Handling multiple exception with single exception.

'''

try:
    a=int(input("Enter Numerator:"))
    b=int(input("Enter Denominator:"))
    c=a/b
    print('Division is:',c)
except Exception:
    print("Something Went Wrong!!")
#except ValueError:
 #   print("Inputs must be a number or digit")
