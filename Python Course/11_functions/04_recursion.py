'''
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
0 1 2 3 4 5 6 7 8 9 10 11 12 13  14  15
fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1) = 0 + 1 = 1
fib(3) = fib(1) + fib(2) = 1 + 1 = 2
fib(4) = fib(2) + fib(3) = 1 + 2 = 3
fin(n) = fib(n-2) + fib(n-1)

'''

def fib(n):
    #Base cases of recursion
    if(n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib(n-1) 
print(fib(6))  # Output: 8