"""
Exception Handling
    try , except , else , finally

a = int(input("Enter A Number: "))
b = int(input("Enter B Number: "))
try:
    print("Division :",a/b)
except:
    print("Division not Possible")
print("Program Completed")

# Custom Error Generate
    assert
    
age = int(input("Enter Age : "))
assert age>17
print("Welcome")


age = int(input("Enter Age : "))
try:
    assert age>17,"Age Should be 18+"
    print("Welcome")
except Exception as e:
    print("Error",e)


Custom Error
    raise


age = int(input("Enter Age : "))
if age<17:
    raise ValueError("Age Should Be 18+")
else:
    print("Welcome")


age = int(input("Enter Age : "))
if age<17:
    raise ZeroDivisionError("Age Should Be 18+")
else:
    print("Welcome")


Custom Exception class


class AgeError(Exception):
    pass
age = int(input("Enter Age : "))
if age<17:
    raise AgeError("Age Should Be 18+")
else:
    print("Welcome")



"""




































