"""
Advance Python
Lambda , Map , Filter , Reduce


def cube(num):
    return num**3

print(cube(9))
print(cube(6))

Lambda expression is used to create small functions/low script function

cube = lambda num: num**3

print(cube(9))
print(cube(6))

add = lambda a,b:a+b

print(add(9,9))

check_even = lambda num: "Even" if num%2==0   else"Odd"

print(check_even(3))
print(check_even(6))

cube = lambda val:val**3
li = [1,2,3,4,5,6,7,8,9,10]
for x in li:
    print(cube(x))

MAP :- MAP can apply a function on every element of a collection

cube = lambda val:val**3
li = [1,2,3,4,5,6,7,8,9,10]
result = list(map(cube,li))
print(result)

# anonymous function
li = [1,2,3,4,5,6,7,8,9,10]
result = list(map(lambda val:val**3,li))
print(result)

result = list(map(lambda val:val**3,[1,2,3,4,5,6,7,8,9,10]))
print(result)

print(list(map(lambda val:val**3,[1,2,3,4,5,6,7,8,9,10])))

# Find all even numbers

li = [23,45,67,79,0,87,56,43,32,56,78,37,69,17]
check_even = lambda num: num if num%2==0 else None
for x in li:
    print(check_even(x))


li = [23,45,67,79,0,87,56,43,32,56,78,37,69,17]
check_even = lambda num: True if num%2==0 else False
for x in li:
    if check_even(x):
        print("Even ",x)
    else:
        print("Odd ",x)


Filter :- Filter can apply a method on a collection and
collect the data if the method return is True

li = [23,45,67,79,20,87,56,43,32,56,78,37,69,17]
check_even = lambda num: True if num%2==0 else False

print(list(filter(check_even,li)))


# Add all the element of a list


li = [x for x in range(1,11)]
add = lambda a,b:a+b
total = 0 
for x in li:
      total = add(total,x)

print(total)


REDUCE 

from functools import reduce
li = [x for x in range(1,11)]
add = lambda a,b:a+b
print(reduce(add,li))

# calculate the sum of all even numbers square of a list

from functools import reduce
li = [1,2,3,4,5,6,7,8,9,10]
result = filter(lambda v:True if v%2==0 else False,li)
result = map(lambda num: num**2,result)
result = reduce(lambda a,b:a+b,result)
print(result)


"""


      






































