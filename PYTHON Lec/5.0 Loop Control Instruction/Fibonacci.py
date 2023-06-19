'''
Fibonacci series
'''
n=int(input("Enter Number:"))
x=0
y=1
print(x)
print(y)
i=1
while i<=n-2:
    z=x+y
    print(z)
    x=y
    y=z
    i=i+1
    
