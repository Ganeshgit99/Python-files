'''
Returning multiple values
==========================
synatx:
    return var1,var2,va3,..........,varn

'''
def airethmetic(x,y):
 add=x+y
 sub=x-y
 mul=x*y
 div=x/y
 return add,sub,mul,div

a,b,c,d=airethmetic(9,2)

print("Addition is:",a)

print("Subtraction is:",b)
print("Multiplication is:",c)
print("Division is:",d)
