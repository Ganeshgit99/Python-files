'''
random module
=============
'''
#Four digit otp generation
import random as r
#print(r.random())
'''
x=r.random()
print(x)
n=x*10000
print(n)
otp=round(n)
print("OTP:",otp)
'''

otp=round(10000*r.random())
print(otp)

y=r.randrange(1000,9999)
print('OTP is:',y)

