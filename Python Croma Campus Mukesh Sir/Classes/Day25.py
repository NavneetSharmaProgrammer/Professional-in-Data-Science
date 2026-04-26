"""
Exception Handling

Type of error

1-Syntax Error
an error in your code can be a typo also but
in this case your code will not run

a = 100
print("Value"a)

interpreter will flag the error while compling

You need to fix the error

2-Runtime Error / Logical Error
An error occur on the console screen at the run time
Interpreter can not flag the error while compling

a = int(input("ENter A Number : "))
b = int(input("ENter B Number : "))

print("Division :",a/b)

This error can not flag by interpreter but it can handle
at the run time and this error is also called exception

3- Symentic Error / human error

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))

print("Addition :",a*b)

This error is a human error or uman logical error
You need to debug it, find the error and fix it




Exception Handling




We can handle a runtime error by using some keywords like


try , except , finally , else


a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except:
    print("We can not divide")
print("Program Complete")

Write the code where you have doubt in the try block
and also mention a alternative code in except block

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except:
    print("We can not divide")
print("Program Complete")

a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    
    print("Division :",a/b)
except ZeroDivisionError as e:
    print("Error :",e)
print("Program Complete")


Exception is the mother class of all exception classes


try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    print(a[9])
except ZeroDivisionError as e:
    print("Error :",e)
except ValueError as e:
    print("Error :",e)
except Exception as e:
    print("Error :",e)
print("Program Complete")


This else block is execute only if there is no error

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except Exception as e:
    print("Error :",e)
else:
    print("Division Complete")
print("Program Complete")



Finally block will execute always

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
    print(a[1])
except ZeroDivisionError as e:
    print("Error :",e)
else:
    print("Division Complete")
finally:
    print("Ye to hamesha chalega")
print("Program Complete")


"""













































