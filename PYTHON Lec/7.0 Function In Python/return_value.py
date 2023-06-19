'''
return statement
==============
1)When there is need to return value from function defination to function call,use return statement.
2)returned value is returned at the place of the function call.
3)Thus there is need of variable to be assigned to function call to store that returned value.
    

'''

def addition(x,y):
    z=x+y
    return z
res=addition(10,20)
print('Addition is:',res)
