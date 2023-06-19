'''
Fibonacci series
'''
n=int(input("Enter Number:"))
x=0
y=1
print(x,end=" ")
print(y,end=" ")
i=1
while i<=n-2:
    z=x+y
    print(z,end=(" "))
    x=y
    y=z
    i=i+1
    
