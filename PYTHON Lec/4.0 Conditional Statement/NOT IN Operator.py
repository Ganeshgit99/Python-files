n=int(input('Enter number between 1 and 10:'))
if n>1 and n<=10:
    if n not in(9,7):
        print("Good")
    else:
        print("Bad")
else:
    print("Please enter between 1 and 10")
