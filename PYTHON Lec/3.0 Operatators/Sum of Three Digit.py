'''
A three digit numbers is entered by user.
Write a program to find sum of its digits.
step 1:Start
Step 2:Message Enter three digit Number
Step 3:store number in x
step 4:Convert in integer and store in 'n'
step 5:digit seperation
step 6:add digit and Store sum
step 7:print sum
step 8:stop
'''
#print("Enter Three digit number")
x=input("Enter Three digit number")
n=int(x)
a=n%10    #a=453%10  =>3
b=n//10   #b=453//10 =>45
c=b%10    #c=45%10   =>5
d=b//10   #d=45//10  =>4

sum=a+c+d
print("Summation is",sum)
