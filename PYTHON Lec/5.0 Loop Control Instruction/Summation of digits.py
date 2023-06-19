'''
Summation of digits of number
'''

n=int(input("Enter Number"))
x=0
while n!=0:
    r=n%10
    x=x+r
    n=n//10
print("Summation of Digits:",x)
