'''
read mode
========
It is used to read data from file.

read():read all data from the file.
readlines():read data line by line. returns list of lines in file.

'''
fp=open('data.txt','r')
data=fp.read()
print("Contact List:")
print(data)
print(data[0])
print(data[1])

print("Using loop:")
for x in data:
    print(x)
