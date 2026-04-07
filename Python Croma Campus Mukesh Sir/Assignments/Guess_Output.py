"""

Precedence  Operator	Description
Highest	    ()	        Parentheses (grouping)
            f(args...),
            x[i], x.attr	Calls, subscriptions, attribute references
            **	        Exponentiation (Right-to-Left)
            +x, -x, ~x	Unary plus, minus, and bitwise NOT
            *, /, //, %	Multiplication, division, floor division, modulo
            +, -	Addition and subtraction
            <<, >>	Bitwise shifts
            &	        Bitwise AND
            ^	        Bitwise XOR
            |	        Bitwise OR
            >, <, >=,
            <=, ==, !=	Comparisons, including identity (is) and membership (in)
            not	        Logical NOT
            and	        Logical AND
            or	        Logical OR
            if - else	Conditional expression
            lambda	Lambda expression
Lowest	    =, +=,
            *=, etc.	Assignment operators




1. What is the output of the following code?
a = 5
b = 10
print(a < b < 20)
True

2. Predict the output:
x = True
y = False
print(x + y * x)
1

3. What does this expression evaluate to?
print(4 ** 0 ** 2)
If the expression were evaluated from left to right, it would be 4 power 0 power 2 = 1 power 2 = 1
Answer 1

4. Find the result of this bitwise operation:
a = 12
b = 5
print(a ^ b)

XOR operator if both are same it give false
      8  4  2  1
12    1  1  0  0
5     0  1  0  1
      1  0  0  1  1001 = 9
      Answer is 9
      
5. Guess the output:
print((3 and 0) or (0 and 3))

   ((3 and 0) or (0 and 3))
     0        or  0
     0 



answer 0

6. What's the output of this tricky comparison?
print(256 is 256)  answer true 
print(257 is 257)  answer true 


7. Evaluate this expression:
a = 7
print(~a + 1)

~ = -(~a + 1)
so
  (-(~a + 1) + 1)
  (-(7 + 1) + 1)
  (-8 + 1)
   -7

8. What will this print?
a = True
b = False
print((a or b) and not (a and b))
     ((1 or 0) and not (1 and 0))
     ((1     ) and not (0      ))
     ((1     ) and     1        )
     ((1                        )
     1 == True
Answer is True

9. What's the output?
print(10 > 5 == True)

When Python sees multiple comparison operators in a row, it rewrites the expression. The expression 10 > 5 == True is interpreted as:

First part: 10 > 5 is True.
Second part: 5 == True is False. In Python, True has a numerical value of 1, and 
 is not equal to 
.
Final result: True and False evaluates to False.


10. Evaluate this expression:
print(2 + 3 * 4 ** 2 // 8 % 3)
     (2 + 3 * 16 // 8 % 3)
     (2 + 48 // 8 % 3)
     (2 + 6 % 3)
     (2 + 0)
     2
     
Answer is 2


11. What does this expression evaluate to?
print(1 << 2 + 1)
     (1 << 3)
                8  4  2  1
1                        1
Add 3 digit     1  0  0  0

     (1 << 3)
     (8)
     
Answer is 8


12. Predict the output:
a = 3
b = 2
a *= b + 1
print(a)

a *= b + 1
a *= 3
9

13. Evaluate this chained comparison:
print(3 < 5 > 2 == 2)
     3 < 5    5 > 2    2 == 2
     1        1        1

14. Guess the result:
print(10 // 3 * 3 + 1 % 3)
     (3 * 3 + 1 % 3)
     (9 + 1 % 3)
     (9 + 1 )
     10
     
15. What is the result of this?
x = 10
y = 20
print(x & y | x ^ y)

16. Trick with boolean and bitwise:
a = True
b = False
print(a & b or a ^ b)

17. Evaluate this:
x = 8
print(x >> 1 << 2)

18. What does this produce?
print(5 + True * False + not False)

error

print(5 + True * False + (not False))
     (5 + True * False + true)
     (5 + 1 * 0 + 1)
     (5 + 0 + 1)
     (6)


19. Operator confusion:
print((not 0) * (False or 1))

(1 * 1)
1

20. Mix of precedence and associativity:
print(4 + 3 * 2 ** 2 // 2 - 1)
     (4 + 3 * 4 // 2 - 1)
     (4 + 12 // 2 - 1)
     (4 + 6 - 1)
     (9)
     

"""






























































