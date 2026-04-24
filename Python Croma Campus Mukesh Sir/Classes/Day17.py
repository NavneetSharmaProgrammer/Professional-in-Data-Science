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

s = {1:34,2:67,4:78,'A':54}
print(s)
print(type(s))
print(s.items())
for k,v in s.items():
    print(k,v)


    get

s = {1:34,2:67,4:78,'A':54}
print(s)
print(s.get(3,"Not Available"))
print(s.get(4,"Not Available"))
# print(s[3])   # it will raise an error



    Update


s1 = {1:34,2:67,4:78,'A':54}
s2 = {6:24,7:46,4:99,9:45}

s1.update(s2)
print(s1)



Built_in functions
    sum ,max, min, len



d = {1:234,2:345,3:456}
print(sum(d))
print(sum(d.values()))
print(max(d.values()))
print(min(d.values()))
print(len(d.values()))


 
'''





































