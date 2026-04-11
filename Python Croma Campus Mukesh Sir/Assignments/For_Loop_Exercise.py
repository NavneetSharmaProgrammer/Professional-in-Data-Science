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


"""
st = input("Enter a String : ")
count = 0
for char in st:
    count += 1
print("Total number of characters:", count)

















