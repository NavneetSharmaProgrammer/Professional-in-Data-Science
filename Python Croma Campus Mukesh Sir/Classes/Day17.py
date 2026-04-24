'''
Dictionary:- Dic is a collection of Key:value pairs

s = {1:34,2:67,4:78,'A':54}     # Key:value => pair (item)
print(s)
print(type(s))

# Dictionary can hold duplicate values
# But can not hold duplicate key
# Dictionary can not sliced
# Dictionary can not replicate
# But dic can be traverse/itterate

s = {1:34,2:67,4:78,'A':54}
print(s)
print(type(s))
for x in s:     # by default it itterate keys
    print(x)

    Dic Methods
    keys , values , items

s = {1:34,2:67,4:78,'A':54}
print(s)
print(type(s))
print(s.keys())
for x in s.keys():
    print(x)

s = {1:34,2:67,4:78,'A':54}
print(s)
print(type(s))
print(s.values())
for x in s.values():
    print(x)

s = {1:34,2:67,4:78,'A':54}
print(s)
print(type(s))
print(s.items())
for x in s.items():
    print(x)

'''
s = {1:34,2:67,4:78,'A':54}
print(s)
print(type(s))
print(s.items())
for k,v in s.items():
    print(k,v)







































