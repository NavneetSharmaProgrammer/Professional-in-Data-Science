# # positional arguments
# def add(a, b):
#     x = a + b
#     return x  # Return the sum of a and b

# c = add(4, 5)
# print(c)  # Output: 9

# # Default arguments
# def add(a, b, plus=0):
#     x = a + b + plus 
#     return x # Return the sum of a, b, and plus

# c = add(4, 5, 1)
# print(c)  # Output: 10 a = 4, b = 5, plus = 1 

# Keyword arguments
def add(a, b, plus=0):
    x = a + b + plus 
    return x  # Return the sum of a, b, and plus
c = add(4, 5, 1)  
print(c)  

c1 = add(b=5, a=4, plus=8)  # Using keyword arguments