"""
While Loop

Syntax:-

initialization
while condition:
    statement
    incr/decr

    Example:-

a = 1
while a<5:
    print("Hello")
    a = a+1

a = 1
while a<=5:
    print("Hello")
    a = a+1


break , continue , pass

a = 1
while a<=5:
    print(a)
    if a == 3:
        break
    a = a+1

a = 1
while a<=5:
    if a == 3:
        continue
    a = a+1
    print(a)

# WAP to print counting from 1 to 10

a = 1
while a<=10:
    print(a)
    a+=1

# WAP to print counting from 1 to 10

a = 1
n = int(input("Enter a number :- "))

while a<=n:
    print(a)
    a+=1

# WAP to print all the factors of a number

a = 1
n = int(input("Enter a number :- "))

while a<=n:
    if n%a==0:
        print(a)
    a+=1

# WAP to add all the digits of a number

num = 375
add = 0
rem = 0
while num>0:
   rem = num%10
   add = add+rem
   num = num//10
print(add)




"""

   

































    











    
    
    
