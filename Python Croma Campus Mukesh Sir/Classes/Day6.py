"""
Control Statement
if , if_else , Nested if_else , elif , complex condition
Loop:- for , while

IF
Ayntax:-
if condition:
    True_Statement
else:
    False_Statement

if 10>5:
    print("Hello")
else:
    print("India")

#WAP to find greater value b/w two
a = 20
b = 10
if a>b:
    print("Greater Value :",a)
else:
    print("Greater Value :",b)

# WAP to check an entered number is Even / Odd

a = int(input("Enter a number :- "))
if a%2==0:
    print("Even",a)
else:
    print("Odd",a)

Nested if_else
#WAP to find greater value b/w two and check equal also

a = 20
b = 30

if a>b:
    print("A is Greater",a)
else:
    if a==b:
        print(f"a{a} == b{b}")
    else:
        print("B is Greater",b)

#WAP to find greater value among three
a=200
b=40
c=5
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)

#Wap to check an entered number is positive , negative , Zero

num = int(input("Enter a number to check it is positive , negative or Zero : - "))

if num > 0:
    print("positive",num)
else:
    if num < 0:
        print("negative",num)
    else:
        print("Zero",num)


ELIF

#Wap to check an entered number is positive , negative , Zero

num = int(input("Enter a number to check it is positive , negative or Zero : - "))

if num > 0:
    print("positive",num)
elif num < 0:
    print("negative",num)
else:
    print("Zero",num)

# WAP to check an character is vowel / consonant
# Vowels:- A,E,I,O,U
ch = input("Enter a number to check vowel / consonant :- ")
if ch=='a' or ch=='A':
    print("Vowel")
elif ch=='e' or ch=='E':
    print("Vowel")
elif ch=='i' or ch=='I':
    print("Vowel")
elif ch=='o' or ch=='O':
    print("Vowel")
elif ch=='u' or ch=='U':
    print("Vowel")
else:
    print("Consonant")




ch = input("Enter a number to check vowel / consonant :- ")
if ch=='a' or ch=='A' or ch=='e' or ch=='E' or ch=='i' or ch=='I' or ch=='o' or ch=='O' or ch=='u' or ch=='U':
    print("Vowel")
else:
    print("Consonant")

    ch = input("Enter a number to check vowel / consonant :- ")
if ch in "AEIOUaeiou":
    print("Vowel")
else:
    print("Consonant")
"""



    

    
























































