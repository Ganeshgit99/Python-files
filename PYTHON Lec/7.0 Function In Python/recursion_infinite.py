'''
Rescursive Function
==================
The function which contains its function call in his body is called as Recursive Function.

'''

x=1
def greet():
    global x
    print("Function Call:",x)
    x=x+1
    greet()
greet()
