'''
Nested loop
=========
One loop inside body of another loop.
There is inner loop and there is outer loop.
For single iteration or repeatition of outer loop inner loop repeat 'n' number of times.

'''

for i in range(1,3,1):
    print(i,end=" - ")
    for j in range(1,4,1):
        print(j,end=" ")

    print()

'''
DRY RUN

#i  print(i)  j  print(j)

1   1        1   1
             2   2
             3   3

2    2       1   1
             2   2
             3   3

'''
