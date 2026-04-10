# name = "Navneet"

# print(name[0:2])  # Output: Na  goes from index 0 to 1

# print(name[2:-1])  # Output: vnee goes from index 2 to second last index

name = "Harry0123456789"

# print(name[0:10:n]) # skips n- 1 characters, where n is the step size
print(name[0:10:1])  # skips 0 characters
print(name[0:10:3])  # skips 3-1 i.e. skips 2 characters

print(name[:4])  # replaces the first empty number with 0, so it is equivalent to name[0:4]
print(name[1:])  # replaces the second empty number with the last index, so it is equivalent to name[1:len(name)]