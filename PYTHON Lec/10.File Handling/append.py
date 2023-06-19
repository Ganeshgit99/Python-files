'''
append:this function add data to the existing data in the file.

syntax:
file_pointer.write()

'''
fp=open('data.txt','a')
n=input("Enter your name:")
mn=input("Enter your Contact Number:")
d=n+':'+mn+"\n"
fp.write(d)
fp.close()
