'''

1)It is collection of dissmimilar elements.Elements in dictionary are arranged in the form of key and value.
2)Elements are enclosed in curly braces.
  {key1:value1,key2:value2,....,ketn:valuen}
3)Key is unique, value can be duplicate.
4)Dictionary are mutable.


'''

d={'a':'apple',1:'One',10.8:1000}
print(d)
print( type(d))
n=len(d)
print("Total Number of elements in Dictionary:",n)

#Accessing value from dictionary with the help of key
'''

syntax:
dict_varchar[keyname]
'''
'''
print(d[1])
print(d['a'])
print(d[10.8])

'''

#for loop over dictionary
'''
for x in d:
    print(x,'-',d[x])

    '''

#Add
'''
synatx:dict_variable[keyname]=value

update()
synatx:dict_variable.update(dictionary)
'''

d['b']='Ball'
print(d)

d1={'c':'cat','pi':3.14}

d.update(d1)
print(d)

#update(replace)
'''
dict_variable[keyname]=newvalue
'''

d['a']='ant'
print(d)

#delete element from dictionary
'''
pop();
syntax:dict_variable.pop(keyname)

del for specific elements
============

del dict_variable[keyname]
To delete entire dictionary
del sict_variable
'''
d.pop(1)
print(d)

del d['pi']
print(d)

del d
print(d)

