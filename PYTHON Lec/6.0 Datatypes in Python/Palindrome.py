'''
Check wheter string is palindrom or not.
e.g
nitin
----->
<-----
'''
s=input("Enter String:")
print("Original String:",s)
sorg=s.upper()
srev=sorg[::-1]
print("Reverse String:",srev)
if sorg==srev:
    print("It is palindrome")
else:
    print("It is not a palidrome")
