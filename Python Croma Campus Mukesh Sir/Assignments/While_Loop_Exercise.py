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


"""
user = int(input("Enter a number : "))
i = 1
f = 1
while i <= user:
    print(i)
    f *= i
    i += 1
print(f"Factorial of {user} is {f}")
    





















