"""
List_Tuple_Questions

Python Programming Questions – LIST
Basic Level

1. Write a Python program to create a list of integers and print its elements.

li = [1,2,3,4,5]
print(li)

li = [1,2,3,4,5]
for i in li:
    print(i)

2. Write a program to find the sum and average of all elements in a list.

li = [1,2,3,4,5]
s = 0
for i in li:
    s += i
print("Sum :",s)
print("Average :",s//i)

3. Write a program to find the largest and smallest element in a list.

li = [1,2,3,4,5]
la = 0
sm = 0
for i in li:
    d = i
    if i>la:
        la = i
    if i<sm:
        sm = i
print("SM",sm)
print("LA",la)

4. Write a Python program to count the number of elements in a list without using len().

li = [1,2,3,4,5]
c = 0
for i in li:
    c += 1
print(c)

5. Write a program to reverse a list without using built-in functions.

"""
li = [1,2,3,4,5]
print(li[5:0:-1])# why 1 not print
print(li[-1:-6:-1])
print(li[5::-1])
print(li[::-1])
print(list(reversed(li)))



    





















