'''
Collections
================
1)String
2)List
3)tuple
4)set
5)dictionary
=========
String
-It is collection of characters.
-Is is immutable.
-strings are defined within single qoute,double qoute,triple qoute.

'''
'''
s1="Itvedant"
print(s1)
s2="Itvedant Pune"
print(s2)
'''
#s3='''This is multiple line string'''
#print(s3)
#print(type(s1))
#print(type(s2))
#print(type(s3))

#len():This Function count number of characters
s="Itvedant"
print(s)
n=len(s)
#print("Total numbers of characters:",n)

#indexing
'''

         I  t  v  e  d  a  n  t
         0  1  2  3  4  5  6  7 =>Positive Indexing
        -8 -7 -6 -5 -4 -3 -2 -1 =>Negative Indexing

accessing single element or character
syntax: variable[index]
'''
'''print(s[5])
print(s[-7])
'''
#slicing
'''

          I  t  v  e  d  a  n  t
          0  1  2  3  4  5  6  7 =>Positive Indexing
         -8 -7 -6 -5 -4 -3 -2 -1 =>Negative Indexing

    slicing gives you substring
    synatx: variable[start:stop:step]
'''

s1=s[2:8:1]
#print(s1)
s2=s[0:8:2]
#print(s2)
s3=s[2:7:] #default step is 1
#print(s3)
s4=s[:8:] #default start is 0
#print(s4)
s5=s[::] #default end is end of srting
#print(s5)
s6=s[6:3:-1]
#print(s6)
s7=s[:3:-1]
#print(s7)
s8=s[::-1]
print(s8)

