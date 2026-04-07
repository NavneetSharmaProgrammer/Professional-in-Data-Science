"""
A. Python IF (Single Condition)

1. Write a Python program to check if a number is positive.
2. Print "Eligible to vote" if age is 18 or above.
3. Check if a number is divisible by 7.
4. Print "Pass" if marks are greater than 40.
5. Check if a number is greater than 100.
6. Display a message if temperature exceeds 45°C.
7. Check if a string length is more than 8 characters.
8. Print "Logged In" if password matches "admin123".
9. Check if a number is a multiple of 10.
10. Print a warning if balance is below minimum limit.


1. Write a Python program to check if a number is positive

num = int(input("Enter a number :- "))

if num > 0:
    print("Positive")
else:
    print("Not Positive")

2. Print "Eligible to vote" if age is 18 or above.

age = int(input("Enter your age"))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

3. Check if a number is divisible by 7.

num = int(input("Enter a number"))

if num%7==0 :
    print("divisible by 7")
else:
    print("Not divisible by 7")

4. Print "Pass" if marks are greater than 40.

marks = int(input("Enter your Marks :- "))

if marks > 40:
    print("Pass")
else:
    print("Fail")

5. Check if a number is greater than 100.

num = int(input("Enter a number"))

if num > 100:
    print("Greater")
else:
    print("Smaller")

6. Display a message if temperature exceeds 45°C.

temp = 47

if temp > 45:
    print("temperature exceeds 45°C")

7. Check if a string length is more than 8 characters.

a ='navneetSharma'
length=len(a)
if length > 8:
    print('more than 8')

8. Print "Logged In" if password matches "admin123".
password ="admin123"
if password == "admin123":
    print("Logged In")

9. Check if a number is a multiple of 10.
num = 25
if num%10==0:
    print("Multiple of 10 ")

10. Print a warning if balance is below minimum limit.
bal = int(input("Enter your balance : "))
if bal < 500:
    print("Below minimum limit")




B. Python IF–ELSE (Two Conditions)

11. Check whether a number is even or odd.
12. Find the largest of two numbers.
13. Check whether a person is eligible for driving license.
14. Print "Pass" or "Fail" based on marks.
15. Check whether a number is positive or negative.
16. Check whether a character is a vowel or consonant.
17. Check if a year is leap or not.
18. Print "Valid Password" or "Invalid Password".
19. Determine whether salary is taxable or not.
20. Check whether a number is greater than 50 or not.v

11. Check whether a number is even or odd.

num = int(input("Enter a number : "))
if num % 2 == 0 :
    print("Even")
else:
    print("Odd")

12. Find the largest of two numbers.

num1 = int(input("Enter 1 number : "))
num2 = int(input("Enter 2 number : "))

if num1 > num2:
    print(num1)
else:
    print(num2)

13. Check whether a person is eligible for driving license.

age = int(input("Enter your age : "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not Eligible for driving license")

14. Print "Pass" or "Fail" based on marks.

Marks = int(input("Enter your marks : "))

if Marks >= 30:
    print("Pass")
else:
    print("Fail")

15. Check whether a number is positive or negative.

num = int(input("Enter a number : "))

if num >= 0:
    print("Positive")
else:
    print("Negative")

16. Check whether a character is a vowel or consonant.

num = input("Enter a character : ")

if num == 'a' or num=='A' or num=='e' or num=='E' or num=='i' or num=='I' or num=='o' or num=='O' or num=='u' or num=='U':
    print("Vowel")
else:
    print("Consonant")

17. Check if a year is leap or not

year = int(input("Enter a year to check leap or not :"))

if year%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")

18. Print "Valid Password" or "Invalid Password".

pas = input("Enter a Password : ")
if pas == 'Navneet1234':
    print("Valid Password")
else:
    print("Invalid Password")

19. Determine whether salary is taxable or not.

salary = int(input("Enter your salary : "))

if salary > 100000:
    print("Taxable")
else:
    print("Not Taxable")

20. Check whether a number is greater than 50 or not.

num = int(input("Enter a number : "))

if num > 50:
    print("Greater than 50")
else:
    print("Less than 50")

C. Python NESTED IF–ELSE

21. Find the largest of three numbers.
22. Check whether a number is positive, negative, or zero.
23. Assign grades:
● A → marks ≥ 90
● B → marks ≥ 75
● C → marks ≥ 60
● Fail → below 60
24. Check whether a triangle is equilateral, isosceles, or scalene.
25. Check whether a character is uppercase, lowercase, digit, or special character.
26. Calculate electricity bill using slab-wise rates.
27. Validate login using username and password.
28. Check student result using marks of 3 subjects.
29. Find the second largest number among three numbers.
30. Check loan eligibility using age, salary, and credit score.

21. Find the largest of three numbers.

a = int(input("Enter 1 number : "))
b = int(input("Enter 2 number : "))
c = int(input("Enter 3 number : "))

if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    print(c)

22. Check whether a number is positive, negative, or zero.

num = int(input("Enter a number : "))

if num > 0:
    print("Positive")
else:
    if num < 0:
        print("Negative")
    else:
        print("Zero")

23. Assign grades:
● A → marks ≥ 90
● B → marks ≥ 75
● C → marks ≥ 60
● Fail → below 60

mar = int(input("Enter your marks : "))

if mar >= 60:
    if mar >= 75:
        if mar >= 90:
            print("A")
        else:
            print("B")
    else:
        print("C")
else:
    print("Fail")

24. Check whether a triangle is equilateral, isosceles, or scalene

a = int(input("Enter a side : "))
b = int(input("Enter b side : "))
c = int(input("Enter c side : "))

if a==b or b==c or c==a:
    if a==b and b==c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    print("Scalene")

25. Check whether a character is uppercase, lowercase, digit, or special character.

char = input("ENTER A CHARACTER : ")

if char >= 'a' and char <= 'z' :
    print('lowercase')
else:
    if char >= 'A' and char <= 'Z' :
        print('uppercase')
    else:
        if char >= '1' and char <= '9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999':
            print('digit')
        else:
            print('special character')

26. Calculate electricity bill using slab-wise rates

print("Press 1 for Urban Domestic Rates (LMV-1 Other) \n Press 2 for Rural Domestic Rates (LMV-1 Rural) ")

area = int(input(""))


if area == 1:
    print("1. Urban Domestic Rates (LMV-1 Other)")
    units = int(input("Enter units consumed : "))
    if units <= 150:
        bill = units*5.50
        print("Slab 1: First 150 units cost ₹5.50 per unit.")
    else:
        if units <= 300:
            bill = 825 + ((units - 150)*6)
            print("Slab 2: Next 300 units (151 to 300) cost ₹6 per unit.")
        else:
            if units > 300:
                bill = 1725 + ((units - 300)*6.50)
                print("Slab 3: Anything over 300 units costs ₹6.50 per unit.")
else:
    if area == 2:
        print("2. Rural Domestic Rates (LMV-1 Rural)")
        units = int(input("Enter units consumed : "))
        if units <= 100:
            bill = units*3.35
            print("Slab 1: First 100 units cost ₹3.35 per unit.")
        else:
            if units <= 150:
                bill = 335 + ((units - 100)*3.85)
                print("Slab 2: Next 150 units (101 to 150) cost ₹3.85 per unit.")
            else:
                if units <= 300:
                    bill = 527.5 + ((units - 150)*5)
                    print("Slab 3: Next 150 units (151 to 300) cost ₹5 per unit.")
                else:
                    if units > 300:
                        bill = 1277.5 + ((units - 300)*5.5)
                        print("Slab 4: Anything over 300 units costs ₹5.5 per unit.")

    else:
        print("Invalid")
print("Total Bill: ₹",bill)





"""


            
    




















    



    



































