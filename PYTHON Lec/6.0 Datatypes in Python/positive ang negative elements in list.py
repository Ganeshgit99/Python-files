'''
Write aprogram to separate positive and negative elements from the list.
'''
l=[10,-1,2,3,67,8,-8,21,-56]
lpos=[]
lneg=list()
print(lpos)
print(lneg)
for x in l:
    if x==0:
        continue
    else:
        if x>0:
            lpos.append(x)
        else:
            lneg.append(x)
print("Original List:",l)
print("Positive List:",lpos)
print("Negative List:",lneg)

