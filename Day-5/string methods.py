Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c = 'Baireddy narasimha Reddy'
len(c)
24
ord('a')
97
char('n')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    char('n')
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(72)
'H'
chr(50)
'2'
min(c)
' '
max(c)
'y'
sorted(c)
[' ', ' ', 'B', 'R', 'a', 'a', 'a', 'a', 'd', 'd', 'd', 'd', 'e', 'e', 'h', 'i', 'i', 'm', 'n', 'r', 'r', 's', 'y', 'y']
c = 'baireedy narasimha reddy'
c
'baireedy narasimha reddy'
c.upper()
'BAIREEDY NARASIMHA REDDY'
c.lower()
'baireedy narasimha reddy'
c.capitalize()
'Baireedy narasimha reddy'
c.title()
'Baireedy Narasimha Reddy'
c.swapcase()
'BAIREEDY NARASIMHA REDDY'
 'baireedy narasimha reddy'.casefold()
 
SyntaxError: unexpected indent
'baireedy narasimha reddy'.casefold()
'baireedy narasimha reddy'
'jfjnSDFCBNMOEDKskdcnjdnf'.caseflod()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    'jfjnSDFCBNMOEDKskdcnjdnf'.caseflod()
AttributeError: 'str' object has no attribute 'caseflod'. Did you mean: 'casefold'?
'jfjnSDFCBNMOEDKskdcnjdnf'.casefold()
'jfjnsdfcbnmoedkskdcnjdnf'
c
'baireedy narasimha reddy'
c.center(60,'*')
'******************baireedy narasimha reddy******************'
c.center(60,'/')
'//////////////////baireedy narasimha reddy//////////////////'
c.center(60,'$')
'$$$$$$$$$$$$$$$$$$baireedy narasimha reddy$$$$$$$$$$$$$$$$$$'
c.ljust(50,'$')
'baireedy narasimha reddy$$$$$$$$$$$$$$$$$$$$$$$$$$'
c.rjust(50,'$')
'$$$$$$$$$$$$$$$$$$$$$$$$$$baireedy narasimha reddy'
'15'.zfill(5)
'00015'
'12'.zfill(34)
'0000000000000000000000000000000012'
c
'baireedy narasimha reddy'
c.find(r)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    c.find(r)
NameError: name 'r' is not defined
c.find('r')
3
c.find('b')
0
c.find('n')
9
c.rfind('s')
13
c.find('d')
6
c
'baireedy narasimha reddy'
c.find('x')
-1
c.count('a')
4
c..count('d')
SyntaxError: invalid syntax
c.count('d')
3
c.index('n')
9
c.rindex('n')
9
c
'baireedy narasimha reddy'
c.replace('i','0')
'ba0reedy naras0mha reddy'
c.replace('reddy','garu')
'baireedy narasimha garu'
c.maketrans('aeiou','23455')
{97: 50, 101: 51, 105: 52, 111: 53, 117: 53}
c.translate(c.maketrans('aeiou','23455'))
'b24r33dy n2r2s4mh2 r3ddy'
c
'baireedy narasimha reddy'
c.split()
['baireedy', 'narasimha', 'reddy']
'baireedy narasimha reddy'
'baireedy narasimha reddy'
'baireedy narasimha reddy'.split()
['baireedy', 'narasimha', 'reddy']
'baireedy narasimha reddy'.split(',')
['baireedy narasimha reddy']
s = '''
... baireddy
... narasimha
... reddy
... '''
>>> s
'\nbaireddy\nnarasimha\nreddy\n'
>>> s.splitlines()
['', 'baireddy', 'narasimha', 'reddy']
>>> ['', 'baireddy', 'narasimha', 'reddy'].join()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    ['', 'baireddy', 'narasimha', 'reddy'].join()
AttributeError: 'list' object has no attribute 'join'
>>> '-'.join(['', 'baireddy', 'narasimha', 'reddy'])
'-baireddy-narasimha-reddy'
>>> s.partition(',')
('\nbaireddy\nnarasimha\nreddy\n', '', '')
>>> s.rpartition(',')
('', '', '\nbaireddy\nnarasimha\nreddy\n')
>>> c.strip()
'baireedy narasimha reddy'
>>> c = '             hello    world'
>>> c
'             hello    world'
>>> c.strip()
'hello    world'
>>> c.lstrip()
'hello    world'
>>> c.rstrip()
'             hello    world'
>>> test = ' hello @'
>>> text.encode()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    text.encode()
NameError: name 'text' is not defined. Did you mean: 'test'?
>>> text.encode()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    text.encode()
NameError: name 'text' is not defined. Did you mean: 'test'?
>>> text = "Hello 🙂"
>>> text.encode()
b'Hello \xf0\x9f\x99\x82'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
