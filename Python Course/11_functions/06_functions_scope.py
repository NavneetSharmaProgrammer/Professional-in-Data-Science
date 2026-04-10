def sum(a, b):
    # a and b are local variables 
    c = a + b
    z = 20  # this will not affect the global variable z. It creates a local variable called z which is destroyed after the function call 
    return c

z = 8  # global variable
print(sum(4, 6))
print(z) # Output: 10
