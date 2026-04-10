# s = "hello world" # Strings are immutable, so we cannot change them
# # name[0] = "R"  # This will raise an error because strings are immutable
# a = len(s)  # Get the length of the string
# print(a)  # Output: 7, the length of the string "Navneet"
# # print(s.upper(), s)  # Convert the string to uppercase and print it along with the original string 
# print(s.lower(),)  # Convert the string to lowercase 
# print(s.title())  # Convert the string to title case
# print(s.capitalize())  # Convert the first character to uppercase and the rest to lowercase 

# text = " \nhello world "
# print(text.strip()) # Output: "hello world"
# print(text.lstrip()) # Output: "hello world " 
# print(text.rstrip()) # Output: hello world"

# # Finding and Replacing
# text = "Python is fun and fun and fun"
# print(text.find("is"))# Output: 7 Index of the first occurrence of "is"
# print(text.replace("fun", "awesome"))# Output: "Python is awesome and awesome and awesome"

# text = "apple,banana,orange"
# print(text.split(","))
# print(text)
# print(",".join(["apple", "banana", "orange"]))

text = "Python123"
print(text.isalpha())# Output: False
print(text.isdigit())# Output: False
print(text.isalnum())# Output: True
print(text.isspace())# Output: False