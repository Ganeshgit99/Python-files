'''
Find Factorial of Number entered by user.
4=1*2*3*4=24
!= Symbol for Factorial
'''
n=int(input("Enter Number"))
i=1
x=1
if n>=0:
    while i<=n:
        x=x*i
        i=i+1
        
    print(n,"!=",x)
else:
    print('Please enter positive number or zero')
    
