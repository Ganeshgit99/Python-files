'''
Amstrong number
================
A three digt number is entered by user.Write a program to check wheter number is amstrong number or not.
'''

n=int(input("Enter three digit number:"))
a=n%10
b=n//10
c=b%10
d=b//10

sum=a*a*a+c*c*c+d*d*d
if sum==n:
    print("Amstrong Number")
else:
    print("Not a Amstrong Number")


'''
Exponent Operator
    n**p  
    '''
#Four digit Number
r=4
p=4
res=n**p #4**4=256

    

