'''
summation of elements

l-[10,3,2,4,80,70]

x     s=0
x=10  s=s+x=0+10=10
x=3   s=s+x=10+3=13
x=4   s=s+x=13+4=15
'''
l=[10,3,2,4,80,70]
s=0
for x in l:
    s=s+x
print("Summation of list elements:",s)
