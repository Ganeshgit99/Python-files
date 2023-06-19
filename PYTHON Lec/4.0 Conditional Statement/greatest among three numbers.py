x=int(input('Enter First Number'))
y=int(input('Enter Second Number'))
z=int(input('Enter Third Number'))
if x>y:
    if x>z:
        print(x,'is greater')
    else:
        print(z,'is greater')
else:
    if y>z:
        print(y,'is greater')
    else:
        print(z,'is greater')

'''
Disadvantages of nested if...else
1)care need to be taken to match if;s with correspondance else's otherwise it gives indentation error.
2)As condition increases program creeps toward right side.

