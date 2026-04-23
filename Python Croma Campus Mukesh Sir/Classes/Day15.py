"""
Tuple :-  Tuple is also a collection and part of sequence
data type like List of hetregenous element,
syntex:-
t = (23,34,45,56,67,78)

Ways to create a tuple

t = (2,45,5,78)
t = (23,'aman',True,3+8j)
t = ()
t = tuple([32,34,45,56])
t = tuple((32,34,45,56))
t = tuple()
print(t)
print(type(t))

Tuple is immutable (You can not change / edit the tuple)
besides List is mutable (You can make changes in list
Tuple is Faster than the List because of its immutability

Tuple works on INDEX
backward  -1,-2,-3,-4..
forward   0,1,2,3,4,5..
tuple_name[index]

t = (234,3,56,67,8,67,0)
print(t)
print( t[2] )
print( t[-5] )


Tuple can be SLICED
tuple_name[start:stop:step]

t = (234,3,56,67,8,67,0)
print(t)
print( t[2:6] )
print( t[-5:-1] )

Tuple can be replicate

t = (234,3,56,67,8,67,0)
print(t)
print( t*3 )



Tuple support Traversing/Itteration
t = (34,67,89,56,34)
print(t)
for x in t:
    print(x)

Built-in Functions
    sum , max , min , len
t = (23,56,67,89)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))
print( sum(t)/len(t) )

Tuple's Method
    index , count

t = (244,23,35,35,24,65,767,34,34,34,45,23,34,34,34,23)
print(t)
print(t.count(34))
print(t.index(34))

    del tuple_name  # to delete the tuple

Nested List

li = [[34,45],[45,87,56]]

Nested tuple

t = ((23,54,67),(54,56,87,45))
li = [[34,45],[45,87,56]]
t = ((23,54,67),(54,56,87,45))

print(f'{li}\n{t}')
print(t[1][2])


t = ([23,45,67],[34,56,76])
li = [ (324,45,67), (34,5,879) ]

li = [ (324,45,67), (34,5,879) ]
print(li)


List Comprehension

li = [ x for x in range(1,21)]
print(li)

# Wap to collect all the even number from 1 to 20 in a list 

li = [ x for x in range(1,21) if x%2==0 ]
print(li)

t = (23,45,[34,75,35],56,34)
print(t)
t[2].append(99)
print(t)

# An object can not lose its behaviour

t = (23,45,'Aman',56,34)
print(t)
print(t[2].upper())

t = (23,45,'Aman',56,34)
print(t)
print(t[2].replace('Aman','Baman'))
print(t)


"""





















