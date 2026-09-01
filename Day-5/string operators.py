Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# String oprations
s =
SyntaxError: invalid syntax
s = ''
s
''
s = 'narsimha'
s
'narsimha'
'narsimha' = 'reddy'
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
'narsimha' + 'reddy'
'narsimhareddy'
'baireddy'*10
'baireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddy'
>>> '-*-'*10
'-*--*--*--*--*--*--*--*--*--*-'
>>> 'baireddy'*10000

>>> 'baireddy'*100
'baireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddybaireddy'
>>> s ='narasimha'
>>> s[4]
's'
>>> s[-1]
'a'
>>> s[-4]
'i'
>>> s = 'Baireddy narasimha reddy'
>>> s[6]
'd'
>>> s[14]
'i'
>>> s[-14]
'a'
>>> s[1:7]
'airedd'
>>> s[2:-1]
'ireddy narasimha redd'
>>> s[17:-17]
''
>>> s[17:-11]
''
>>> #s[start:end+1:step]=>s[0:len:1]
>>> s[-1:-6:-1]
'ydder'
>>> s[::-1]
'ydder ahmisaran ydderiaB'
>>> s[::2]
'Bied aaih ed'
>>> 'narasimha' in s
True
>>> 'reddy' in s
True
>>> 'garu' not in s
True
