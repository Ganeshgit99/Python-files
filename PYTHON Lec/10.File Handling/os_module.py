'''
os module
========

'''
#getcwd()
'''
This function given absolute path of current working folder or directory.

'''
#listdir()
'''
This function return list of all files and folder in that location.
By default it returns list list of files and folder from same directory in ehich pythoin files is saved.

'''
import os
'''
import os
cpath=os.getcwd()
print("Current Path of folder",cpath)
'''
'''
l=os.listdir()
print(l)
for x in l:\
    print(x)
'''

#mkdir()
'''
This Function crete new folder
'''
'''
os.mkdir('student')
l=os.listdir()
print(l)
'''


#rename directory or folder
'''
syntax:
os.rename(oldname,newname)
'''
'''
l=os.listdir()
print(l)
os.rename('student','student_info')
l=os.listdir()
print(l)
'''
#file rename
'''
l=os.listdir()
print(l)
os.rename('data.txt','datainfo.txt')
l=os.listdir()
print(l)
'''
#delete directory
'''
os_rmdir(directory name)
'''
'''
l=os.listdir()
print(l)
os.rmdir('student_info')
l=os.listdir()
print(l)
'''

#delete file
'''
os.rename(filename)
'''

l=os.listdir()
print(l)
os.remove('datainfo.txt')
l=os.listdir()
print(l)







