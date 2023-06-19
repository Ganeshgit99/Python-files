ms=input("Enter Name to be searched:")

fp=open('data.txt','r')

data=fp.readlines()
single=0
for x in data:
    l=x.split(":")
    #l[0].upper()==ms.upper()
    if l[0].upper()==ms.upper():
        print(x)
        single=1
if single==0:
    print("RECORD NOT FOUND!!")
