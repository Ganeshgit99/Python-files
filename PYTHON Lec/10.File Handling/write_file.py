'''
Need of file
============
1.Variables store data temporary.
2.To store data permanetly there is need of file.

open file:
open(filename,mode)
This open() function returns you file pointer which is reference of file in tour python code.

modes
=====
1.r=>read mode
2.w=>write mode
3.a=>append mode

To write into file
====================
Syntax:
file_pointer.write(data)
'''

fp=open('data.txt','w')
#print(fp)

n="Itvedant Pune"
m="98989877"
d=n+':'+m
fp.write(d)

fp.close()#to close and save data in file


'''
In write mode new data always overwrite previous data.
If there is need to preserve previous data and new data must be added at the end then open file in append mode.


'''
