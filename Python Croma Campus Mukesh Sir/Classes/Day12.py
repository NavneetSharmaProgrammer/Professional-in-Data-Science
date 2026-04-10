"""
Random Liabrary

import Library_name

import random
#random.random() return a value between 0 to 1
print(random.random())
print(random.random()*100)
print(random.random()*1000)


import random
# print(random.randint(1,10)) return a value from 1 to 10
# print(random.randint(1,6)) return a value from 1 to 6
# print(random.randint(1000,9999)) return a value from 1000 to 9999 laike a otp


# Number Guessing Game
1-7
you have guess that random number and you have only 3 chance

"""
import random
num = random.randint(1,7)
for i in range(1,4):
    print(i,"Chance!")
    u = int(input("Guess A Number From 1 to 7 : "))
    if num == u:
        print("You Guess The Right Number")
        print("That was The Random Number ",num)
        print("Reward Points : ",30//i,"out of 30")
        break
else:
    print("You Lose!")
    print("The right number was ",num)
    

























































