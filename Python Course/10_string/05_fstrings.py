# String formatting

template = "Dear {}, You are awesome! Take this {}$ coupon."
n1 = "Navneet"
c1 = 100
n2 = "Rohit"
c2 = 200
n3 = "Ravi"
c3 = 300

s1 = template.format(n1, c1)
print(s1)  # Output: Dear Navneet, You are awesome! Take this 100$ coupon.

# String formatting using f-strings

print(f"{n1} you are awesome! Take this {c1}$ coupon.")  # Output: Navneet you are awesome! Take this 100$ coupon.
