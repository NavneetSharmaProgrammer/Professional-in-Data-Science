"""
for loop
# break , continue , pass

for i in range(1,5):
    if i==3:
        break
    print(i)
else:
    print(0)

for i in range(1,5):
    print(i)
    if i==3:
        break
else:
    print(0)


for i in range(1,5):
    print(i)
    if i==4:
        break
else:
    print(0)


for i in range(1,5):
    print(i)
    if i==5:
        break
else:
    print(0)

for i in range(1,9,2):
    if i%0b110==0:
        break
    print(i)

for i in range(1,9,2):
    if 0b110%i==0:
        break
    print(i)

for i in range(1,9):
    if i%0b110==0:  # 1%6 2%6-----6%6  1 2 3 4 5 
        break
    print(i)



Nested For

# WAP to check a number is prime

num = 17
count = 0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("Prime",num)

WAP to find all the prime numbers from 1 to 100

for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("Prime",num)


PATTERN PRINTING

*****
*****
*****
*****
*****

print("*****")
print("*****")
print("*****")
print("*****")
print("*****")

print("*****\n*****\n*****\n*****\n*****")

print("*****\n"*5)


for i in range(1,6):
    for j in range(1,6):
        print("*",end='')
    print()


*
**
***
****
*****

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()

1
12
123
1234
12345

for i in range(1,6):
    num=0
    for j in range(1,i+1):
        num += 1
        print(num,end='')
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()


1
22
333
4444
55555

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()

1
23
456
78910

num = 0
for i in range(1,6):
    for j in range(1,i+1):
        num +=1
        print(num,end='')
    print()


"""
num = 0
for i in range(1,6):
    for j in range(1,i+1):
        num +=1
        print(num,end='')
    print()






    
  

    




















































































