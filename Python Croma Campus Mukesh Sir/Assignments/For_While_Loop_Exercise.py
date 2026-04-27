"""
FOR Loop – Programming Questions
1. Write a program to print numbers from 1 to 100.

for i in range(1,101):
    print(i)

2. Write a program to print all even numbers between 1 and 50.

for i in range(2,51,2):
    print(i)

3. Write a program to print the sum of first n natural numbers.

n = 4
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)

4. Write a program to print the multiplication table of a given number.

n = int(input("Enter a number to print the multiplication table : "))
m = 0
for i in range(1,11):
    m = i*n
    print(f"{n} * {i} = {m}")

5. Write a program to print all elements of a list using a for loop.

l = [1,2,3,4,5,6,7,8,9,"a",'b','c','d','e','f','g','h','i']
for i in l:
    print(i)

6. Write a program to count the number of vowels in a string.

s = "Navneet Sharma"
c = 0
for i in s:
    print(i)
    if i in "aeiouAEIOU":
        c = c+1
print("Number of vowels : ",c)

7. Write a program to find the largest number in a list.

l = [1,8,3,4,6,5]
m = 0
for i in l:
    if m < i :
        m = i
print(m)

8. Write a program to print all prime numbers between 1 and 100.

for i in range(2,101):
    is_prime = True
    for j in range(2,i):
        if i%j==0:
            is_prime = False
            break
    if is_prime:
        print(i)

9. Write a program to calculate the factorial of a number using a for loop.

n = int(input("Enter a number : "))
f = 1
for i in range(1, n+1):
    f = f*i
print("factorial of a number ",f)

10. Write a program to print the reverse of a string using a for loop.

rs = ""
s = input("Enter a string to reverse: ")

for i in s:
    rs = i + rs
print(rs)


WHILE Loop – Programming Questions


11. Write a program to print numbers from 1 to 50 using a while loop.

n = 50
i = 0
while i < n:
    i += 1
    print(i)

12. Write a program to print all odd numbers between 1 and 50.

n = 50
i = 1
while i < n:
    print(i)
    i += 2

13. Write a program to calculate the sum of digits of a number

n = 234
on = n
tsum = 0
while n > 0:
    ld = n % 10
    tsum += ld
    n = n//10
print("The sum of the digits in", on , "is:", tsum)

14. Write a program to reverse a number using a while loop.

n = int(input("Enter a number to reverse: "))
ld = 0
r = 0
while n > 0:
    ld = n%10
    n = n//10
    r = (r * 10)+ ld
    print("Extracted:", ld)
print("Final Reversed String:", r)

15. Write a program to find the factorial of a number using a while loop.

n = int(input("Enter a number to find the factorial : "))
f = 1
i = 1
while i<=n:
    f *= i
    i +=1
print(f'Factorial of {n} is {f}')

16. Write a program to keep taking input from the user until the user enters 0.

while True:
    n = input('Enter a number ')
    if n == '0':
        break

17. Write a program to find the largest digit in a number

n = int(input("Enter a number : "))
ld = 0
b = 0
while n > 0:
    ld = n % 10
    n = n//10
    if b < ld:
        b = ld
print("Largest digit",b)

18. Write a program to check whether a number is a palindrome.

n = int(input("Enter a number : "))
i = 0
while i < n:
    p = i
    p = p**3
    if n == 1:
        print("Palindrome")
    elif p == n:
        print("Palindrome")
        break
    elif i+1 == n:
        print("Not palindrome")
    i = i+1

19. Write a program to print the Fibonacci series up to n terms.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377
a  b  c
   a  b  c

n = int(input("Enter a number : "))
a = 0
b = 1
i = 1
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(a)
else:
    # If n is 2 or more, we can safely print the first two terms
    print(a)
    print(b)
while i < n-1:
    c = a+b
    a = b
    b = c
    print(c)
    i = i+1

20. Write a program to implement a number guessing game using a while loop.

print("\t\t### Number Guessing Game ###")
n = 4
g = 0
p = 10
while n != g:
    g = int(input("\n\t\tEnter a number between 1 to 10 : "))
    if n == g:
        print("\n\t\tYou win! ")
    elif p == 0:
        print("You Lose")
        break
    else:
        print("\n\t\tWrong Guess again!")
    p -= 1
print(f"\n\t\tYour points is {p}")

22. Write a program to count the frequency of each character in a string.

"""


 
    








































