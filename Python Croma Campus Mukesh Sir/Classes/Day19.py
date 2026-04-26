"""
String :- String is also a collection of characters and
it behave like a tuple.
It means string is also immuteable, you can not change
anything in the string

s = "Navneet Sharma"

s = ""
s='aman'
s="aman"
s='''aman'''
s=str("aman")
s=str(2737)
print(s)
print(type(s))

String can work on INDEX (backward and forward)
Streing can be sliced

s = "amankumar"
print(s[-7:-2])

String can be replicate

print("Ha"*3)


String can be traverse\itteration
s = "AMANKUMAR"
for x in s:
    print(x)

Built-in Functions
    sum , max , min , len
Characters works on ASCII value
a = 97 , b = 98 , c = 99 ---- z = 122
A = 65 , B = 67 ------------- Z = 90
0 = 48 , 1 = 49 ------------- 9 = 57


s = "AmanKumar"
print( s )
print( max(s) )
print( min(s) )
print( len(s) )


String's Method
    upper , lower , capitalize

s = "Aman Kumar"
print( s )
print( s.upper() )
print( s.lower() )
print( s.capitalize() )

join , strip
s = '  aman     '
print(s)
print( s.strip() )   # it will remove over space from both sides

s = "PYTHON"
print( "$"+s )
print( "$".join(s) )
s = ['aman','kumar','is','my','brother']
print( "$".join(s) )
print( " ".join(s) )

    isalpha , isalnum , isdigit

s = 'aman'
print( s.isalpha() )
print( s.isdigit() )
print( s.isalnum() )
s = 'aman128'
print( s.isalpha() )
print( s.isdigit() )
print( s.isalnum() )
s = '34'
print( s.isalpha() )
print( s.isdigit() )
print( s.isalnum() )


"""




























































