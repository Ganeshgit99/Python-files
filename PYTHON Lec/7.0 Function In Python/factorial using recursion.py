'''
Factorial of a number using recursion

'''

num=int(input("Enter Last term:"))
def factorial(n):
    if n==1:
        return 1
    s=n*factorial(n-1)
    return s
res=factorial(num)
print("Factorial is:",res)
