'''
Set
====
1)It is collection of disimilar datatype.
2)They are mutable.
3)Sets are enclosed in curly or flower braces.
4)There is no index for elements in set.
5)All elements are unique or set doesn't allow duplicate elements.
6)We can add and remove set elemnts 
'''
s={10,20,-3,'Itvedant',90.8,10}
print(s)
print(type(s))
n=len(s)
print("Total Number of elements in sets:",n)

#indexing
#There is no index in set

#slicing
#Since there is no index in set, slicing is not possible

#loop over set elements

for x in s:#{10,20,-3,'Itvedant',90.8,10}
    print(x)

#add element in set
'''
add(value):
This method is used to add elements in set.
syntax:
set_variable.add(value)
'''

s.add(100)
print(s)

#update(iterable)
s1={2,3,40}
s.update(s1)
print(s)

l=[1000,250]
s.update(l)
print(s)

t=(15,30)
s.update(t)
print(s)

#remove elements from set.
'''
discard(value) and remove(value)
'''

s.discard(100)
print(s)

s.remove(30)
print(s)

#discard:The discard() method removes the specified item from the set.
#remove(): the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

del s
print(s)

