"""
Python While Loop Exercise
Part 1 – Basic Level
1. Print numbers from 1 to 10 using a while loop.

i = 1
while i <= 10:
    print(i)
    i += 1

2. Print even numbers from 1 to 20.

i = 2
while i <= 20:
    print(i)
    i += 2

3. Print odd numbers from 1 to 20.

i = 1
while i <= 20:
    print(i)
    i += 2

4. Print numbers from 10 to 1 (reverse order).

i = 10
while i >= 1:
    print(i)
    i -= 1

5. Print multiplication table of 5 using while loop.

i = 1
while i <= 10:
    print(f"5 * {i} = {i*5}")
    i += 1

Part 2 – Intermediate Level
6. Find the sum of first 10 natural numbers using while loop.

n = 1
s = 0
while n <= 10:
    print(n)
    s += n
    n += 1
print(f"Sum of first 10 natural number is {s}")


7. Find factorial of a number entered by user.

user = int(input("Enter a number : "))
i = 1
f = 1
while i <= user:
    print(i)
    f *= i
    i += 1
print(f"Factorial of {user} is {f}")

8. Count number of digits in a given number.

num = 234
count = 0
while num > 0:
    num = num//10
    count = count +1
print(count)

9. Reverse a number using while loop.

num = 234
reverse_num = 0
while num > 0:
    last_digit = num%10
    print("l",last_digit)
    reverse_num = (reverse_num*10)+last_digit
    print("reverse_num",reverse_num)
    num = num//10
print(reverse_num)

10. Check whether a number is palindrome or not using while loop.



Part 3 – Pattern Based
11. Print pattern:
*
**
***
****
*****

s = "*"
user = 5
i = 1
while user >= i:
    print(s*i)
    i +=1

12. Print pattern:
1
12
123
1234
12345

Part 4 – Logical / Real Scenario
13. Ask user to enter password until correct password is entered.

while True:
    user = input("Enter Password : ")
    pas = "Navneet@321"
    if user == pas:
        break
print("Login Successfully")

14. Create a number guessing game:
• Generate a random number (1–10)
• Keep asking user until they guess correctly


15. Keep taking input numbers until user enters 0, then print total sum.


16. Print Fibonacci series up to N terms using while loop.
0 1 1 2 3 5 8 13 21 34 55 89.....
  a b
0 1 1
a b c


a = 0
b = 1
terms = 10
i = 1
while i<=terms:
    c = a + b
    print(c)
    a = b
    b = c
    i +=1



"""
num = 1
add = 0
while num != 0:
    num = int(input("Enter a number : "))
    add += num
print("Total ",add)



























