'''

Searching
1.By mobile number
2.By Name
'''

ms=input("Enter Mobile number to be searched:")

fp=open('data.txt','r')

data=fp.readlines()
for x in data:
    print(x)
    l=x.split(":")
    #print(l[1])
    #print(int(ms)==int(1[1]))
    if int(ms)==int(l[1]):
        print(x)
        break
else:
    print("Record Not Found!!")
