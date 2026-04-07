"""
7- Bitwise Operator
    and => &
    or  => |
    not => !

    32  16  8  4  2  1
19       1  0  0  1  1
28       1  1  1  0  0

&        1  0  0  0  0   16
|        1  1  1  1  1   31

a = 19
b = 28
print(a and b)
print(a & b)
print(a | b)

     64  32  16  8  4  2  1
25    0   0   1  1  0  0  1
56    0   1   1  1  0  0  0

&         0   1  1  0  0  0   24
|         1   1  1  0  0  1   57

a = 25
b = 56
print(a&b)
print(a|b)


not ~
a = -5
print( ~a )
# -(x+1)



Right Shift Operator   >>
Left Shift Operator    <<

>>   64  32  16  8  4  2  1
18    0   0   1  0  0  1  0
10010            1  0  0  1   9  remove last 1 digit 
10010               1  0  0   4  remove last 2 digit 
10010                  1  0   2  remove last 3 digit
10010                     1   1  remove last 4 digit
10010                         0  remove last 5 digit
10010                         0  remove last 6 digit

a = 18
print(a>>1)
print(a>>2)
print(a>>3)
print(a>>4)
print(a>>5)
print(a>>6)

<<   64  32  16  8  4  2  1
9     0   0   0  1  0  0  1
1001          1  0  0  1  0   18   Add last 1 digit
1001      1   0  0  1  0  0   36   Add last 2 digit
1001  1   0   0  1  0  0  0   72   Add last 3 digit

a = 9
print(a<<1) 
print(a<<2)
print(a<<3)



^ XOR
XOR:-  if both inputs are same, then the output is False otherwise True

True XOR True  = False

^      64  32  16  8  4  2  1
21      0   0   1  0  1  0  1
38      0   1   0  0  1  1  0
            1   1  0  0  1  1  51  both same false

a = 21
b = 38

print(a^b)
 """



























