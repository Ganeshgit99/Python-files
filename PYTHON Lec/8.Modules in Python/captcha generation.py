'''
Five letters captcha generation
==============================

'''


#create source string
import string as s
import random as r
source=s.ascii_letters+s.digits
print(source)

c=''
for i in range(0,5):
    rindex=r.randrange(0,62)
    print('Index:',rindex)
    ch=source[rindex]
    print("Character at index",rindex ,'is:',ch)
    c=c+ch
    print(c)
    print()
print("Captcha:",c)

