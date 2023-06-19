'''
1)Need of logical operator to check more than one condition in single if statment.
2)To remove disadvantages of nested if...else.
'''
#Program

x=int(input("Enter First Number"))
y=int(input("Enter Second Number"))
z=int(input("Enter Third Number"))

if x>y and x>z:
    print(x,'is greater')

if y>x and y>z:
    print(y,'is greater')

if z>x and z>y:
    print(z,'is greater')
    
