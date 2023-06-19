'''
Varable length argument.
====================
Number of argument in function is argument length.

'''

def addition(*x):
    #print(type(x))
    #print(x)
    s=0
    for i in x:
        s=s+i
    print("Additon is:",s)
addition(10)
addition(10,20)
addition(10,20,30)

