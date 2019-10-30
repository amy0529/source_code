Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import keyword
keyword.kwlist
SyntaxError: multiple statements found while compiling a single statement
>>> import keyword

>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print (a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print (a)
NameError: name 'a' is not defined
>>> a
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=0
>>> print(a)
0
>>> one=two=three=10
>>> print(one,two,three)
10 10 10
>>> one,two,three=10,10,10
>>> print(one,two,three)
10 10 10
>>> print('''
     this is OK!
     ''')

     this is OK!
     
>>> print(
	'OK')
OK
>>> b=''
>>> print(b)

>>> b=' '
>>> print(b)
 
>>> name='Tom'
>>> name1='Jerry'
>>> name2='''Steck'''
>>> print(name,name1,name2,'<Tom &Jerry')
Tom Jerry Steck <Tom &Jerry
>>> name,name1,name2='Tom',"Jerry",'''Sreck'''
>>> print(name,name1,name2,"<tom&Jerry>")
Tom Jerry Sreck <tom&Jerry>
>>> name[1]
'o'
>>> name='Tom'
>>> job='teacher'
>>> name+','+job
'Tom,teacher'
>>> record=name+','+job
>>> print(record)
Tom,teacher
>>> record[0]='t'
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    record[0]='t'
TypeError: 'str' object does not support item assignment
>>> name
'Tom'
>>> record
'Tom,teacher'
>>> record[4:]
'teacher'
>>> record[:]
'Tom,teacher'
>>> 10.0/3
3.3333333333333335
>>> 10*2+0.1
20.1
>>> 1.1+0.9
2.0
>>> 4.0/2.0
2.0
>>> 4.0/2
2.0
>>> e
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    e
NameError: name 'e' is not defined
>>> e2
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    e2
NameError: name 'e2' is not defined
>>> 0.2*0.3
0.06
>>> print '0b1110'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('0b1110')?
>>> print('0b1110')
0b1110
>>> 0b1110
14
>>> bin(3)
'0b11'
>>> bin(14)
'0b1110'
>>> 0b1110<<2
56
>>> 0b00110101&0b0110001
49
>>> 0b00110101&0b01100001
33
>>> 0b00110101|0b01100001
117
>>> bin(117)
'0b1110101'
>>> ascii(117)
'117'
>>> ascii(u)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ascii(u)
NameError: name 'u' is not defined
>>> ascii('u')
"'u'"
>>> 0b00110101^0b01100001
84
>>> bin(84)
'0b1010100'
>>> ~0b00110101
-54
>>> bin(-54)
'-0b110110'
>>> ~00110101
SyntaxError: invalid token
>>> ~0b00110101
-54
>>> 11001010
11001010
>>> ~110000
-110001
>>> ~0b110000
-49
>>> bin(-49)
'-0b110001'
>>> ~a
-1
>>> ~0b1
-2
>>> ~1
-2
>>> ~3
-4
>>> bin(7)
'0b111'
>>> chr(-54)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    chr(-54)
ValueError: chr() arg not in range(0x110000)
>>> char(1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    char(1)
NameError: name 'char' is not defined
>>> chr(1)
'\x01'
>>> chr(33)
'!'
>>> 0b00110101<<2
212
>>> bin(212)
'0b11010100'
>>> chr(212)
'Ô'
>>> 0b00110101>>2
13
>>> 
