"""
Collections
a = 24
a = 55
List , Tuple , Set , Dictionary
Sequential Data Type
    List , Tuple

List :- List is a collection of hetregenous (different)
data type elements
syntax:-    [34,54,24,54,65]

Different ways to create a list

li = [34,56,34,65,35,57,46,13]
li = [34,23.53,True,'aman',3+9j,'A']
li = []
li = list([62,783,64])
li = list((62,783,64))
print(li)
print(type(li))



List works on INDEX
Backword -1, -2, -3, .....
Forward 0, 1, 2, 3, 4, 5......
list_name[index]

li = [34,54,67,89,46]
print(li)
print(li[3])
print(li[-4])

List can be SLICED
List_name[start:stop:step]

li = [34,54,67,89,46]
print(li)
print(li[1:3])
print(li[1:3:1])
print(li[1:4])
print(li[1:4:2])
print(li[-1:-4:-1])
print(li[-4:-2])

List can be replicate

li = [1,2,3,4,5]
print(li)
print(li*3)

List can be traversed/itterate

li = [34,56,78,90,53]
print(li)
for x in li:
    print(x)


Built-in Functions
    sum , max , min , len

li = [23,43,45,56,66,78,79,23]
print(li)
print(sum(li))
print(max(li))
print(min(li))
print(len(li))
print(sum(li)/len(li))


LIst Methods
    append, extend, insert

li = [23,78,79,23]
print(li)
li.append(99)
print(li)
li.insert(2,12)#li.insert(index,value)
print(li)
li2 = [222,333,444]
li.extend(li2)
print(li)


    POP, REMOVE, CLEAR, DEL(Keyword)

    li = [23,78,79,23,43,45,56,66,78,79,23]
print(li)
li.pop()
print(li)
li.pop(3)#pop(index)
print(li)
li.remove(23)# remove(value)
print(li)
del li[1]
print(li)
li.clear()
print(li)
del li
print(li)



sort, reverse

li = [234,264,23,7,246,364,46]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

    count , index

li = [234,23,23,264,23,7,246,234,234,364,46]
print(li)
print(li.count(23))
print(li.index(23))
print(li.index(23,3))  # index(value,start)

    copy
"""
li = [234,264,23,7,246,364,46]
abc = li.copy()
abc[1] = 99
print(abc)
print(li)











































