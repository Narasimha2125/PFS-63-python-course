Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
  l =[1, 2, 3, 4, 5]
  
SyntaxError: unexpected indent
l = [1,2,34,5]
l
[1, 2, 34, 5]
id(l)
1666764398592
l.append(1)
l
[1, 2, 34, 5, 1]
id(l)
1666764398592
i.insert(1,13)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    i.insert(1,13)
NameError: name 'i' is not defined. Did you mean: 'id'?
l.insert(1,13)
l
[1, 13, 2, 34, 5, 1]
id(l)
1666764398592
l.extend(34,63,97)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l.extend(34,63,97)
TypeError: list.extend() takes exactly one argument (3 given)
l.extend([26,628,2245])
l
[1, 13, 2, 34, 5, 1, 26, 628, 2245]
id(l)
1666764398592
l[5]
1

l
[1, 13, 2, 34, 5, 1, 26, 628, 2245]
l[45]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l[45]
IndexError: list index out of range
id()l
SyntaxError: invalid syntax
id(l)
1666764398592
l.pop()
2245
l
[1, 13, 2, 34, 5, 1, 26, 628]
l.pop()
628
l.pop(3)
34
l
[1, 13, 2, 5, 1, 26]
l.remove()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l.remove()
TypeError: list.remove() takes exactly one argument (0 given)
l.remove(1)
l
[13, 2, 5, 1, 26]
del l[5]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    del l[5]
IndexError: list assignment index out of range
del l[2]
l
[13, 2, 1, 26]
l.clear()
l
[]
1
1
l
[]
l = [1,2,3,845,426649,54,2]
l
[1, 2, 3, 845, 426649, 54, 2]
max(l)
426649
min(l)
1
l.sorted()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    l.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
l
[1, 2, 3, 845, 426649, 54, 2]
sorted(l)
[1, 2, 2, 3, 54, 845, 426649]
l
[1, 2, 3, 845, 426649, 54, 2]
l.reverse()
l
[2, 54, 426649, 845, 3, 2, 1]
l
[2, 54, 426649, 845, 3, 2, 1]
l.sort()
l
[1, 2, 2, 3, 54, 845, 426649]
l.sor(reverse=True)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    l.sor(reverse=True)
AttributeError: 'list' object has no attribute 'sor'. Did you mean: 'sort'?
l.sort(reverse=True)
l
[426649, 845, 54, 3, 2, 2, 1]
sum(l)
427556
l =  [1,2,3]
m = [1,2,3]
l
[1, 2, 3]
m
[1, 2, 3]
l
[1, 2, 3]
n = l
n.append(5)
n
[1, 2, 3, 5]
ll
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    ll
NameError: name 'll' is not defined. Did you mean: 'l'?
>>> l
[1, 2, 3, 5]
>>> m = l.copy()
>>> m
[1, 2, 3, 5]
>>> m.append(16)
>>> m
[1, 2, 3, 5, 16]
>>> l
[1, 2, 3, 5]
>>> all([0,'',[],(),set(),{},False])
False
>>> all([1,'',[1,2],(),set(),{},False])
False
>>> ([0,'',[1,23],(),set(),{},False])
[0, '', [1, 23], (), set(), {}, False]
>>> any([0,'',[1,2],(),set(),{},False])
True
>>> l
[1, 2, 3, 5]
>>> l.index(2)
1

>>> l.count(4)
0
>>> l.count(3)
1
>>> l = [[1,2,3,4],[5,6,7,8]]
>>> l
[[1, 2, 3, 4], [5, 6, 7, 8]]
>>> l[0]
[1, 2, 3, 4]
>>> 1[1]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    1[1]
TypeError: 'int' object is not subscriptable
>>> l[1]
[5, 6, 7, 8]
>>> l[0][3]
4
>>> l[1][2]
7
>>> l[-1][-1]
8
