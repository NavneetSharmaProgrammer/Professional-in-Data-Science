"""
Pattern Programming


1
12
123
1234
12345


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


1
01
010
1010
10101


k = '0'
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end="")
        k=k+'1'
    print()


k = 1
m = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end="")
        k=k-m
        m=-m
    print()


k = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(k%2,end="")
        k=k+1
    print()


A
AB
ABC
ABCD
ABCDE

for i in range(1,6):
    for j in range(1,i+1):
        print("A",end='')
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end='')
    print()


for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end='')
    print()



A
BB
CCC
DDDD
EEEEE

for i in range(1,6):
    for j in range(1,i+1):
        print(chr(i+64),end='')
    print()


for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end='')
    print()


A
BC
DEF
GHIJ
KLMNO

k = 65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(k),end='')
        k+=1
    print()


    *
   **
  ***
 ****
*****

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print("*",end='')
    print()

    * 
   * * 
  * * * 
 * * * * 
* * * * *

for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print("* ",end='')
    print()


1
22
333
4444
55555

for i in range(1,6):
    print(str(i)*i)


1
12
123
1234
12345

st =""
for i in range(1,6):
    st = st+str(i)
    print(st)

A
AB
ABC
ABCD
ABCDE

st =""
for i in range(1,6):
    st = st+chr(i+64)
    print(st)

0
909
89098
7890987
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321


"""
st ="0"
for i in range(10,0,-1):
    if i!=10:
        st = str(i)+st+str(i)
    print(st)














