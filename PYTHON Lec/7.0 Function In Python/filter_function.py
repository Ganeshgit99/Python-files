'''
filter(function,iterable)
'''

l=[1,-9,80,4,78,-4,-2]

lpos=list(filter(lambda x:x>0,l))
print(lpos)

leven=list(filter(lambda x:x%2==0,l))
print(leven)


