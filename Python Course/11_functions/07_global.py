def sum(a, b):
    print("HEy I am summing")
    c = a + b
    global z # Please modify the global variable z
    z = 20  # This will refer to the global variable z and not create a local variable
    return c

z = 3
print(sum(3, 12))  # Output: 15
print(z)  # Output: 3