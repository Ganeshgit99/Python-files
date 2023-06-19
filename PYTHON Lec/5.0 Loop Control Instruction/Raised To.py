n=int(input("Enter Number"))
p=int(input("Enter Power"))
i=1
x=1
if n>=0 and p>=0:
    while i<=p:
        x=x*n
        i=i+1

    print(n,'^',p,'=',x)
else:
    print("Invalid inputs either number or power or both")
