Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 20
b = 10
a+b
30
a-b
10
a*b
200
a%b
0
a/b
2.0
9/2
4.5
9%2
1
4**2
16
a<b
False
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
c = 10
ac = c+10
ac = c+10
c
10
c = c+10
c
20
c += 10
c
30
c -= 10
c
20
c //= 10
c
2
c &= 2
c
2
c %= 4
c
2
c **= 5
c
32
c $= 2
SyntaxError: invalid syntax
c != 2
True
c /= 9
c
3.5555555555555554
true and false
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    true and false
NameError: name 'true' is not defined. Did you mean: 'True'?
n=10
n%2==0
True
n%==3
SyntaxError: invalid syntax
n%3==0
False
n5
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    n5
NameError: name 'n5' is not defined. Did you mean: 'n'?
N%2==0 and n%3==0
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    N%2==0 and n%3==0
NameError: name 'N' is not defined. Did you mean: 'n'?
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n
10
n<5
False
not n<5
True
# str list tuple set
 s = 'codegnan'
 
SyntaxError: unexpected indent
s='codegnan'
g in s
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    g in s
NameError: name 'g' is not defined
'g' in s
True
'a' in s
True
'b' in s
False
'b' not in s
True
l=[1, 2, 3, 4]
4 in l
True
8 in l
False
9 not in l
True
t=(1, 2, 3, 4)
3 in t
True
4 not in t
False
8 not in t
True
6 in t
False
s={1, 2, 3, 4}
2 in s
True
4 in s
True
8 in s
False
5 not in s
True
dict = {'name' : 'narasimha', 'age' : '22', 'batch' : 'CSE'}
name in dict
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    name in dict
NameError: name 'name' is not defined
'name' in dict
True
'narasimha' in dict
False
'age' in dict
True
'CSE' in dict
False
l = [1, 2, 3, 4]
m = [5, 6, 7, 8]
id(l)
2205872029376
id(m)
2205872029312
l is m
False
n  = 1
n  = 1
id(n)
140707395965864
n = l












id(n)
2205872029376
n is m
False
n is not m
True
id(a)
140707395966472
s = {1, 2, 3, 4}
id(s)
2205871787584
s.add(9)
s
{1, 2, 3, 4, 9}
id(s)
2205871787584
l = [1, 2, 3, 4]
id(l)
2205871958336
l.add(l)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    l.add(l)
AttributeError: 'list' object has no attribute 'add'
l.add(7)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    l.add(7)
AttributeError: 'list' object has no attribute 'add'
#Bitwise operatar
9&8
8
5^8
13
6|3
7
8>>2
2
4<<6
256
4<<1
8
~8
-9
~4
-5
a = 10
b = 10.3
c = narasimha
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    c = narasimha
NameError: name 'narasimha' is not defined
c = 'narasimha'
>>> print(a,b,c)
10 10.3 narasimha
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"| b value is",b,"| c value is",c,)
a value is 10 | b value is 10.3 | c value is narasimha
>>> print(a,b,c,sep=')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print(a,b,c,sep='')
...       
1010.3narasimha
>>> print(a,b,c,sep='\n')
...       
10
10.3
narasimha
>>> print(a,b,c,sep='\t')
...       
10	10.3	narasimha
>>> print(a,b,c,sep='\n\t')
...       
10
	10.3
	narasimha
>>> print(a,b,c,sep='\@')
...       
10\@10.3\@narasimha
>>> print(a,b,c sep=@)
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(f'a={a} b={b} c={c}')
...       
a=10 b=10.3 c=narasimha
>>> print(f'a value is {a} | b value is {b} | c value is {c}')
...       
a value is 10 | b value is 10.3 | c value is narasimha
>>> print('a=%d b=%f c%s'%(a,b,c))
...       
a=10 b=10.300000 cnarasimha
>>> print('a=%d b=%2.f c=%s'%(a,b,c))
...       
a=10 b=10 c=narasimha
>>> print('a=%d b=%.2f c=%s'%(a,b,c))
...       
a=10 b=10.30 c=narasimha
