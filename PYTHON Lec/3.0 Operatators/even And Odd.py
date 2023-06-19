'''
Need of decision  control instruction
==========================================
When there is need to execute a portion of a code or set instruction based ont he condition,use decision control instruction.

Types of decision control instruction/statement
====================================================
1)if statement
2)if..else statement
3)nested if..else
4)logical operators
5)elif statement

if statment
==============
syntax:
if condition:
    body of it or
    code to be executed

=======================
if...else statement
syntax:
if condition:
    body of it or
    code to be executed

else:
    body of it or
    code to be executed

working:
========
if condition is True,then code in if block is executed.
if condition is False,then code in else is executed.  
'''
'''
Oue)A number is enter by the user.Write a program to check w
'''
n=int(input("Enter a number:"))
r=n%2
if r==0:
   print("Even Number")
else:
    print("Odd Number")
