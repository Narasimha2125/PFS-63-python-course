# Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# print('***SETS***')
# ***SETS***
# s = {}
# type(s)
# <class 'dict'>
# s = set()
# type(s)
# <class 'set'>
# s = {1, 2, 3, 4, 5, ,686, 3456, 233456}
# SyntaxError: invalid syntax
# s
# set()
# s = {1, 2, 3, 4, 5, 6, 6778, 76, 23}
# s
# {1, 2, 3, 4, 5, 6, 76, 23, 6778}
# s.add(1000)
# s.add(2.4)
# s.add(2+4j)
# s.add('SETS')
# s.add([1, 2, 3])
# Traceback (most recent call last):
#   File "<pyshell#13>", line 1, in <module>
#     s.add([1, 2, 3])
# TypeError: unhashable type: 'list'
# s.add((1, 2, 3))
# s.add({1, 2, 3})
# Traceback (most recent call last):
#   File "<pyshell#15>", line 1, in <module>
#     s.add({1, 2, 3})
# TypeError: unhashable type: 'set'
# s.add({1:2})
# Traceback (most recent call last):
#   File "<pyshell#16>", line 1, in <module>
#     s.add({1:2})
# TypeError: unhashable type: 'dict'
# s.add(True)
# s.add(False)
# s
# {False, 1, 2, 3, 4, 5, 6, 2.4, 1000, (1, 2, 3), 76, (2+4j), 23, 6778, 'SETS'}
# s = {1, 1, 1, 1, 1}
# s
# s
# {1}
# s = {10, 20, 30}
# m = {1, 2, 3}
# s+m
# Traceback (most recent call last):
#   File "<pyshell#25>", line 1, in <module>
#     s+m
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# s * 2
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     s * 2
# TypeError: unsupported operand type(s) for *: 'set' and 'int'
# s[0]
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     s[0]
# TypeError: 'set' object is not subscriptable
# s[::-1]
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     s[::-1]
# TypeError: 'set' object is not subscriptable
# s = {1, 2, 3, 4, 5}
# m = {3, 5, 7, 9}
# s
# {1, 2, 3, 4, 5}
# m
# {9, 3, 5, 7}
# s | m
# {1, 2, 3, 4, 5, 7, 9}
# s & m
# {3, 5}
# s - m
# {1, 2, 4}
# s ^ m
# {1, 2, 4, 7, 9}
# {1} < a
# Traceback (most recent call last):
#   File "<pyshell#37>", line 1, in <module>
#     {1} < a
# NameError: name 'a' is not defined
# {1} < s
# True
# {1, 2, 3, 4, 5} < s
# False
# {1, 2, 3, 4, 5} <= a
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#     {1, 2, 3, 4, 5} <= a
# NameError: name 'a' is not defined
# {1, 2, 3, 4, 5} <= s
# True
# s >= {1}
# True
# s >= {1, 2, 3, 4, 5}
# True
# s >= {1, 2, 3, 4}
# True
# s.isdisjoint(b)
# Traceback (most recent call last):
#   File "<pyshell#45>", line 1, in <module>
#     s.isdisjoint(b)
# NameError: name 'b' is not defined
# s.isdisjoint(m)
# False
# a.isdisjoint({9, 10})
# Traceback (most recent call last):
#   File "<pyshell#47>", line 1, in <module>
#     a.isdisjoint({9, 10})
# NameError: name 'a' is not defined
# s.isdisjoint({9, 10})
# True
# a.union(b)
# Traceback (most recent call last):
#   File "<pyshell#49>", line 1, in <module>
#     a.union(b)
# NameError: name 'a' is not defined
# s.union(m)
# {1, 2, 3, 4, 5, 7, 9}
# s.intersection(m)
# {3, 5}
# s.difference(m)
# {1, 2, 4}
# s.symmetric_difference(m)
# {1, 2, 4, 7, 9}
# s.issuperset(m)
# False
# 1 in s
# True
# 6 in s
# False
# 8 not in m
# True
# max(s)
# 5
# min(a)
# Traceback (most recent call last):
#   File "<pyshell#59>", line 1, in <module>
#     min(a)
# NameError: name 'a' is not defined
# min(s)
# 1
# sorted(a)
# Traceback (most recent call last):
#   File "<pyshell#61>", line 1, in <module>
#     sorted(a)
# NameError: name 'a' is not defined
# sorted(s)
# [1, 2, 3, 4, 5]
# len(s)
# 5
# sum(s)
# 15
# a = s
# b.add(354456)
# Traceback (most recent call last):
#   File "<pyshell#66>", line 1, in <module>
#     b.add(354456)
# NameError: name 'b' is not defined
# a.add(12345)
# a
# {1, 2, 3, 4, 5, 12345}
# s
# {1, 2, 3, 4, 5, 12345}
# >>> c = s.copy()
# >>> c.add(11)
# >>> c.add(12)
# >>> c
# {1, 2, 3, 4, 5, 12345, 11, 12}
# >>> s
# {1, 2, 3, 4, 5, 12345}
# >>> s.add(6)
# >>> s
# {1, 2, 3, 4, 5, 6, 12345}
# >>> s.update({7, 8})
# >>> s
# {1, 2, 3, 4, 5, 6, 7, 8, 12345}
# >>> s.pop()
# 1
# s
# >>> 
# >>> s
# {2, 3, 4, 5, 6, 7, 8, 12345}
# >>> s.pop()
# 2
# >>> s
# {3, 4, 5, 6, 7, 8, 12345}
# >>> s.pop()
# 3
# >>> s
# {4, 5, 6, 7, 8, 12345}
# >>> s.remove(6)
# >>> s
# {4, 5, 7, 8, 12345}
# >>> s.discard(6)
# >>> s
# {4, 5, 7, 8, 12345}
# >>> s.discard(3)
# >>> s
# {4, 5, 7, 8, 12345}
# >>> s.clear()
# >>> s
# set()
