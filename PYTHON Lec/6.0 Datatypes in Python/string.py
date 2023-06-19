'''
Write A program to count number of vowels and consonants in astring given by user
'''
'''
str="itvedant"

v=0  c=0
1.select character x='i'
2.i x in(a,e,i,o,u........)

v=v+1 - 0+1=1

v=1  c=0
1.select character x='t'
2.t x in(a,e,i,o,u........)

c=c+1 - 0+1=1 
'''
#Dryrun
"""
x  x in(a,e...U)  v=v+1    c=c+1
i  i in ()        v=0+1=1      --
t  t in ()         --      c=0+1=1

"""

str=input("Enter Character")
v=0
c=0
for x in str: #'itvedant'

    if x in ('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    else:
        c=c+1
print("Total Number of Vowels:",v)
print("Total Numbers of cinstants:",c)
