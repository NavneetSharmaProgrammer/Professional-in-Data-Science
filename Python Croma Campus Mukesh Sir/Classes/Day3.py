"""
Operators


a+b   =>   a,b => Operand   , => Operator
Operator operates on operands

Types of operators
     - Unary Operators   ( -5 , ~5 not false )
     - Binary Operators  ( 10-5 )

1- Arithmetic Operators
    + - * % / // **
a = 7
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a%b)# % (modulus) it is used to calculate the remainder
print(a/b)
print(a//b)# // Truncation/Floor Divison (it divides but return integer value (Removes point/Decimal values) )
print(a**b)# ** Exponential (it is used to calculate power)
print(2**5)# 2*2*2*2*2

2- Assignment Operators
=
a = 10 # 10 is assign to a
a += 1 # a = a+1
a *= 2 # a = a*2
print(a)
3- Relational / Conditional Operators
> < >= <= == != (return boolean) (boolean True / False)

a = 7
b = 5
print(a>b)
print(a<b)
print(a>=b) # is greater than or equial to
print(a<=b) # is less than or equal to
print(a!=b) # is not equal to
print(a==b) # is equal to

4- Membership Operator ( check existance )
   in , not in         ( Return Boolean Answer )
a = "Navneet"
b = "Navneet Sharma"
print( a in b )
print( 'N' in b)
print( 'NS' in b)
print( 'n' in b)
print( 'n' not in b)
print( 's' in b)
print( 's' not in b)


a = [1,2,3]
b = [1,2,3]
print( a in b )
c = [1,2,[1,2,3],3]
print( a in c )

5- Identity Operator (check exact match) (check memory)
   is , is not (Return Boolean Answer)
   
a = "aman"
b = "amankumar"
c = "aman"
print(a is b)
print(a is c)
print(a is not b)

a = [1,2,3]
b = [1,2,3]
print( a is b )

a = "aman"
b = "aman"

6- Logical Operator
    and or not  (return boolen answer)

and => if both conditions are True, Result is True otherwise False

print( 10>5 and 30>5)
print( 10>5 and 30>50)
print( 10>50 and 30>50)

or => if both conditions are False, Result is False otherwise True

print( 10>50 or 30>50 )  
print( 10>50 or 30>5 )
print( 10>5 or 30>5 )

not => It is also called Invertor gate
it accept only and only one input
if input is True, result is False and vice-versa

print( 10>5 )
print( not 10>5 )

print( not (10>5 and 10>4) )


print(int(True))
print(int(False))

print(bool(1))
print(bool(0))
print(bool(196388))
print(bool(-782378))
print(bool("amdkj"))
print(bool(False))

print( True > False )  
print( True + True*False )
print( True*True + False*False )
print( True + ( 10>5 and 20>50 ) )

"""










