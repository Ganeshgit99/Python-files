'''
tuple:
1)It is collection of dissimilar elements
2)tuple are reprented by round brackets(parenthesis)
or elements of tuple are enclosed in parenthisis.
3)they are immutable.
'''

t=(10,'Itvedant',89.9,'Pune',97,100)
print(t)
#dataype
print(type(t))
#len()
n=len(t)
print('Total number of elements in tuple:',n)

#indexing
'''

        (10,'Itvedant',89.9,'Pune',97,100)
         0      1        2     3    4  5
         -6     -5      -4    -3   -2  -1
'''
#print(t[3])
#print(t[-5])

#slicing
tsub=t[1:4:1]
#print(tsub)

trev=t[::-1]
#print(trev)

#for loop with index

for i in range(0,len(t),1):
    print(t[i])
print("For loop without index")
for x in t:
    print(x)
    
#t[3]="Pune city"
#print(t)

del t
print(t)
