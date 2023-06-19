'''
Filtering is done ont he basis of certain condition,
In order to check condition we use if...else or if statment.
So in program involving filtering usinf loop, there is need to use if statment for condition inside loop.
Syntax:

for i in range(start,stop,step):

    if condition:

      do something
'''

#Find all numbers in multiple of 3 between 1 to 100.

for i in range(1,101,1):
    print(i)
    r=1%3
    if r==0:
        print(i)

