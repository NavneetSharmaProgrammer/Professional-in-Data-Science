"""
UDF:- User Define Functions
Functions:- A function is a collection of statements and
perform a specific task and return a value.

Syntax:-
def function_name(parameter):
    statements

function_name(argument)

Example:-

def greet(val):
    print("Good",val)

greet("Night")
greet("Afternoon")

def greet(val):
    return"Good "+val

print(greet("Night"))
print(greet("Afternoon"))

# Wap to check a number is prime or not

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num = int(input("Enter a number : "))
if isPrime(num) and num!=1:
    print("Prime")
else:
    print("Not Prime")

    
# WAP to find all the prime number from 1 to 100


def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(1,101):
    if isPrime(i) and i!=1:
        print(i)

        
"""

   

            


















   





