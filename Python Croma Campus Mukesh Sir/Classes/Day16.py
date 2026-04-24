"""
SET
SEt is also a collection of unique hetregeneous elements 
Syntax:-
s = { 43,65,76,98,34 }

s = { 43,65,76,98,34 }
print(s)
print(type(s))

s = {34,45,56.45,'Aman',True}
print(s)


s = {8,4,6,3,2,6,8,5,3,1,4,6,8,7,6,5,4,3,2,1,2,3,6,4,3,2,6,7,65,54,765,43}
print(s)
# it will remove the duplicate value from the set
# order is not preserved
# set has no index
# set can not be sliced
# set can not be replicate
# set can be traverse/itterate
s = {23,89,56,26,73}
print(s)
for i in s:
    print(i)

Set can work with Built-in Functions
    sum , max , min , len
    
s = {23,89,56,26,73,56}
print(s)
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

Set Method
    add,pop,remove,discard,del(Keyword),clear

s = {23,89,56,26,73,56,356}
print(s)
s.add(99)
s.add(999)
s.add(111)
print(s)
s.pop()
print(s)
s.remove(999)
print(s)
s.remove(356)
print(s)
# remove (222) # it will raise an error
s.discard(23)
print(s)
s.discard(222)
print(s)
s.clear()
print(s)
del s 
print(s)

    union , intersection , difference , symmetric_difference


s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print( s1 )
print( s2 )
print( s1.union(s2) )
print( s1.difference(s2) )
print( s1.intersection(s2) )
print( s1.symmetric_difference(s2) )

    Set operation



s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
print(s1|s2) # union
print(s1&s2) # intersection
print(s1-s2) # difference
print(s1^s2) # Symmetric_difference


"""





























