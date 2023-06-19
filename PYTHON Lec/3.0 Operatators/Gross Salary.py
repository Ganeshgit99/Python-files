'''
Basic salary.Write a program where user enter basic salary and get gross salary as output.
'''
print("Enter Basic Salary")
x=input()
a=float(x)
hra=a*0.2
da=a*0.5
ta=a*0.3
gs=a+hra+da+ta
print("Gross Salary is:",gs)
