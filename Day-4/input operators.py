Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> x = input()
narasimha 
>>> x
'narasimha '
>>> name = input()
Baireddy
>>> name
'Baireddy'
>>> name = input('enter the name :')
enter the name : Baireddy
>>> name
' Baireddy'
>>> age = input("enter the age")
enter the age : 22
>>> age
' : 22'
>>> type(age)
<class 'str'>
>>> names = input('enter the names :')
enter the names :Baireddy Narasimha Reddy
>>> names
'Baireddy Narasimha Reddy'
>>> names.split()
['Baireddy', 'Narasimha', 'Reddy']
>>> names = ('enter the names : ').split()
>>> names
['enter', 'the', 'names', ':']
>>> nmaes = input('enter the names :').split()
enter the names :1 2 3 4 5 6 
>>> names
['enter', 'the', 'names', ':']
>>> nmaes
['1', '2', '3', '4', '5', '6']
>>> map(int,names)
<map object at 0x00000290A6865DB0>
>>> list(map(int,names))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    list(map(int,names))
ValueError: invalid literal for int() with base 10: 'enter'
>>> values = list(map(int,input().split()))
1 2 3 4 5 6
>>> values
[1, 2, 3, 4, 5, 6]
>>> values = list(map(float,input().split()})
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
values = list(map(float,input().split()}
              
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
values = list(map(float,input().split()))
              
values
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    values = list(map(float,input().split()))
ValueError: could not convert string to float: 'values'
values = list(map(float,input().split()))
              
1 2 3 45 6 7 
values
              
[1.0, 2.0, 3.0, 45.0, 6.0, 7.0]
names = tuple(input('enter the names :').split()
              1 2 3 4 5 6
              
SyntaxError: '(' was never closed
names = tuple(input('enter the names :').split())
              
enter the names :1 2 3 4 5 6  
names
              
('1', '2', '3', '4', '5', '6')
names = tuple(map(input('enter the names ;').split()))
              
enter the names ;1 234 4  6 3 
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    names = tuple(map(input('enter the names ;').split()))
TypeError: map() must have at least two arguments.
names = tuple(map(input('enter the names :').split()))
              
enter the names :1 2 3 4 56 6 7 
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    names = tuple(map(input('enter the names :').split()))
TypeError: map() must have at least two arguments.
names = tuple(map(int,input('enter the names :').split()))
              
enter the names :1 2 3 4 5 6 7
names
              
(1, 2, 3, 4, 5, 6, 7)
names = tuple(map(float,input().split()))
              
1 2 3 4 56 7 8 
names
              
(1.0, 2.0, 3.0, 4.0, 56.0, 7.0, 8.0)
names = set(map(int,input().split()))
              
1 2 3 45 6 
names
              
{1, 2, 3, 6, 45}
a,s = [1,2]
              
a
              
1
s
              
2
a,s = (1,2)
              
a
              
1
s


s
              
2
email,password =input('enter the email and password: ').split()
              
enter the email and password: narsimha20@gmail.com,1234
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    email,password =input('enter the email and password: ').split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password =input('enter the email and password: ').split()
              
enter the email and password: 
baireddy2@GMAIL.com and 12345
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    email,password =input('enter the email and password: ').split()
ValueError: not enough values to unpack (expected 2, got 0)
email,password =input('enter the email and password: ').split()
              
enter the email and password: Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    email,password =input('enter the email and password: ').split()
ValueError: too many values to unpack (expected 2)
email,password =input("enter the email and password: ").split()
              
enter the email and password: narasimha@gmail.com 1234
email
              
'narasimha@gmail.com'
password
              
'1234'
a,b,c = list(map(int,input().split()))
              
1 2 3 
a
              
1
s
              
2
b
              
2
c
              
3
nmae,marks = input().split()
              
narasimha 22
name
              
' Baireddy'
marks
              
'22'
int(marks)
              
22
e  eval(input())
              
SyntaxError: invalid syntax
e = eval(input())
              
1
e
              
1
e = eval(input())
              
1234.754
e
              
1234.754
e = eval(input))
              
SyntaxError: unmatched ')'
e = eval(input())
              
[1,2,3,4,]
e
              
[1, 2, 3, 4]
e = eval(input())
{1,2,3,4,5,6}
              
SyntaxError: multiple statements found while compiling a single statement

