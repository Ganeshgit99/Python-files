'''
1)List is collection of diffrent datatypes.
2)List is represented by square brackets[].
3)list is mutable.

'''

#defination
l=[10,'Itvedant',25.6,'Pune']
print(l)
#datatype
print(type(l))
#len():To count number of elements
n=len(l)
print(n)

#indexing
'''

        [10,'Itvedant',25.6,'Pune']
         0      1        2     3
         -4    -3       -2    -1

Accesing list element
list_variable[index]
'''

#print(l[1])
#print(l[-2])

#slicing
#list_variable[start:stop:step]
'''

        [10,'Itvedant',25.6,'Pune']
         0      1        2     3
         -4    -3       -2    -1

'''
"""
l1=l[0:3:1]
print(l1)

lrev=l[::-1]
print('Reversed list is:',lrev)

#for loop over list
print("for loop with index:")
for i in range(0,len(l),1):
    print(l[i])
print("for loop without index:")
for x in l:
    print(x)
"""

#add element in list
'''
1)append():Thsi method add element at the end of the list.
2)insert():This method add element at specific position.
    synatax:
    list_variable.insert(index position,value)
'''

l.append(100)
print(l)
l.insert(3,'Pune city')
print(l)

#update or raplace
'''

list_variable[index]=new values
'''

l[5]='online'
print(l)

#pop():Remove last element from list
l.pop()
print(l)
l.pop(4)#delete element by index
print(l)
l.remove(25.6)#delete element by value
print(l)

#delete entire list

del l
print(l)

