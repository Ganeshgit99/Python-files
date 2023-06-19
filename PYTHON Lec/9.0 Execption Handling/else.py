'''

try..except and else
=====================
1.It is recommended that not to overload try block with those instruction in which there is no chance of getting execption.
2.Those statements in which there is no chance of getting exception must be included in else block.

'''

try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    c=a/b
    
except Exception:
    print("Something Went Wrong!!")
else:
    print('Division is:',c)
#finally:
 #   print("In Finally Block!!")
'''
Working of else block

It execute the code when there is no error 
'''
