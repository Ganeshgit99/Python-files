'''
Summation of 1 to n.
'''

num=int(input("Enter Last term:"))
def summation(n):
    if n==1:
        return 1
    s=n+summation(n-1)
    return s
res=summation(num)
print("Summation is:",res)
