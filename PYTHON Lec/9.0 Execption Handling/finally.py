try:
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))
    c=a/b
    print('Division is:',c)
except Exception:
    print("Something Went Wrong!!")
finally:
    print("In Finally Block!!")
    
