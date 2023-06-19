'''
Summation of ! to n
'''

n=int(input('Enter Last term'))
i=1  #initialization
x=0
while i<=n:
    x=x+i
    i=i+1
print("Summation is:",x)
