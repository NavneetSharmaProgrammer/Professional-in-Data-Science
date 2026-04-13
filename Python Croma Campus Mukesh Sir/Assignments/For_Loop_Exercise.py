"""
PART 1 – Basic For Loop Questions

Q1. Print Numbers
Use a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)

num = 0
for i in range(1,11):
    num +=1
    print(num)

Q2. Print Even Numbers
Print all even numbers between 1 and 20

for i in range(2,21,2):
    print(i)

num = 0
for i in range(1,11):
    num +=2
    print(num)

Q3. Find Sum
Print the sum of numbers from 1 to 10 using a for loop.

su = 0
for i in range(1,11):
    su +=i
    print(i)
print("sum of all number ",su)


Q4. Multiplication Table
Take a number from the user and print its multiplication table up to 10.

table = int(input("Enter a number to print multiplication table : "))

for i in range(1,11):
    print(f"{table} * {i} = {table*i}")


Q5. Count Characters
Take a string and count the total number of characters using a for loop.

st = input("Enter a String : ")
count = 0
for char in st:
    count += 1
print("Total number of characters:", count)



PART 2 – Break Related Questions



Q6. Stop at 5
Print numbers from 1 to 10.
Stop the loop when the number becomes 5.

for i in range(1,11):
    print(i)
    if i == 5:
        break



PART 6 – Pattern Questions


Q16. Star Pattern
Print:
*
**
***
****
*****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end = '')
    print()

Q17. Reverse Star Pattern
Print:
*****
****
***
**
*

rows = 6
for i in range(6,0,-1):
    for j in range(1,i):
        print("*",end = '')
    print()

Q18. Number Pattern
Print:
1
12
123
1234
12345

num = ""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()

Q19. Same Number Pattern
Print:
1
22
333
4444
55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()


Q20. Pyramid Pattern
Print:
    *
   ***
  *****
 *******
*********

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end='')
    for j in range(1,i*2):
        print('*',end='')
    print()

Q21. Inverted Pyramid

Print:
***********
 *********
  *******
   *****
    ***
     *

rows = 6
for i in range(rows,0,-1):
    for k in range(6,i,-1):
        print(" ",end='')
    for j in range(1,i*2):
        print('*',end='')
    print()


Bonus Question
Q22. Break in Pattern
Print a star pattern.
Stop printing when the row number reaches 4.

for i in range(1,6):
    if i>4:
        break
    for j in range(1,i+1):
        print("*",end="")
    print()

"""





        
        
        

















