"""
Looping:- Looping is a concept from which you can execute a
piece of code again and again for a finite times.

Loops:- for , while
FOR
Syntax:-

for variable_name in range(start , stop , step):
    statements 

print( *range(1,11,1))
print( *range(2,21,2))

for example:-
for a in range(1,5,1): # for 1 in 1 2 3 4
    print('hello')

for a in range(1,10,2):
    print('India')

for a in range(12,121,12):
    print(a)

# By default value for step is 1 
for a in range(1,10):
    print(a)


# By default value for step is 1 
# By default value for start is 0 
for a in range(5):
    print(a)

#WAP to print 1 to 10 counting
for a in range(1,11):
    print(a)

for a in range(-1,-10,-1): # 
    print(a)

#WAP to print counting from 1 to N
n = int(input("Enter range from 1 to : "))
for a in range(1,n+1):
    print(a)

# WAP to print TAble of a number
n = int(input("Enter a number : "))
for a in range(n,n*10+1,n):
    print(a)

n = int(input("Enter a number : "))
for a in range(1,11):
    print(a*n)

#WAP to print factors of a number
# HINT:-    12 => 1,2,3,4,6,12

n = int(input("Enter a number to find factor:"))

for a in range(1,n+1):
    b=n
    if b%a==0:
        print(a)

n = int(input("Enter a number to find factor:"))

for a in range(1,n+1):
    if n%a==0:
        print(a)
# range() method do not accept float value

# WAP to count factors of a number
# HINT:-  12 => 1,2,3,4,6,12 => 6 Factors

count = 0
n = int(input("Enter a number to find factor:"))

for a in range(1,n+1):
    if n%a==0:
        count = count + 1
        print(a)
print("Total Factor : ",count)

# WAP to check a number ia prime or not






"""
count = 0
n = int(input("Enter a number to find factor:"))

for a in range(1,n+1):
    if n%a==0:
        count = count + 1
        print(a)
print("Total Factor : ",count)
if count==2:
    print("Prime")
else:
    print("Not Prime")





































































