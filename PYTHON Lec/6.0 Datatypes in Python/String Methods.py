'''
String Methods:
synatx:
string.variable.methodname()
1)lower()  2)upper()  3)capitalize()
'''
'''
s="Itvedant pune offline lecture"
print(s)
s1=s.upper()
print(s1)

slo=s1.lower()
print(slo)

scap=s.capitalize()
print(scap)

stitle=s.title()
print(stitle)
'''

'''
isaplha(),isalnum() and isdigit()
These methods return True or False
'''
'''
s=input("Enter String")

res=s.isalpha()
#res=s.isalnum()
print(res)
'''
'''
split():It is used to break or split string

synatx:
    string_variable.split('delimeter')
'''

s="itvedant-pune-offline-lectures"
res=s.split('-')
print(res)
print(type(res))

#By default separator is Space
