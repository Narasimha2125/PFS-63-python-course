# Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# print('**DICT***')
# **DICT***
# d = {}
# type(d)
# <class 'dict'>
# d = dict()
# type(d)
# <class 'dict'>
# d = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# d
# {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# id(d)
# 1417671139392
# d['k4'] = 'v4'
# d
# {'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
# id(d)
# 1417671139392
# d['k1'] = 'v11'
# d
# {'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
# d['k5'] = 'v4'
# d
# {'k1': 'v11', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4', 'k5': 'v4'}
# d = {}
# d[1] = 'int'
# d
# {1: 'int'}
# d[1.2] = 'float'
# d
# {1: 'int', 1.2: 'float'}
# d[3+5j] = 'complex'
# d
# {1: 'int', 1.2: 'float', (3+5j): 'complex'}
# d['Hello'] = 'String'
# d
# {1: 'int', 1.2: 'float', (3+5j): 'complex', 'Hello': 'String'}
# d[(1, 2, 3)] = 'tuple'
# d[False] = 'Boolean'
# d
# {1: 'int', 1.2: 'float', (3+5j): 'complex', 'Hello': 'String', (1, 2, 3): 'tuple', False: 'Boolean'}
# d[frozenset({1, 2, 3})] = 'frozenset'
# d
# {1: 'int', 1.2: 'float', (3+5j): 'complex', 'Hello': 'String', (1, 2, 3): 'tuple', False: 'Boolean', frozenset({1, 2, 3}): 'frozenset'}
# d[[1, 2, 3, 4, 5]] = 'list'
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
#     d[[1, 2, 3, 4, 5]] = 'list'
# TypeError: unhashable type: 'list'
# d

# d
# {1: 'int', 1.2: 'float', (3+5j): 'complex', 'Hello': 'String', (1, 2, 3): 'tuple', False: 'Boolean', frozenset({1, 2, 3}): 'frozenset'}
# d[{1, 2, 3}] = 'set'
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     d[{1, 2, 3}] = 'set'
# TypeError: unhashable type: 'set'
# d[{1:2}] = 'dict'
# Traceback (most recent call last):
#   File "<pyshell#33>", line 1, in <module>
#     d[{1:2}] = 'dict'
# TypeError: unhashable type: 'dict'
# d = {}
# d[1] = 1
# d[2] = 1.23
# d[3] = 1+6j
# d[4] = 'string'
# d[5] = [1, 2, 3]
# d[6] = (1, 2, 3)
# d[7] = {1, 2, 3}
# d[8] = {1:1}
# d[9] = True
# d
# {1: 1, 2: 1.23, 3: (1+6j), 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
# 9 in d
# True
# 10 in d
# False
# 'string' in d
# False
# {1, 2, 3} in d
# Traceback (most recent call last):
#   File "<pyshell#48>", line 1, in <module>
#     {1, 2, 3} in d
# TypeError: unhashable type: 'set'
# >>> 10 not in d
# True
# >>> d[5]
# [1, 2, 3]
# >>> d[8]
# {1: 1}
# >>> d[10]
# Traceback (most recent call last):
#   File "<pyshell#52>", line 1, in <module>
#     d[10]
# KeyError: 10
# >>> d.get(10)
# >>> d.get(1)
# 1
# >>> d.get(10, 'Key is not present')
# 'Key is not present'
# >>> d.get(6, 'Key is not present')
# (1, 2, 3)
# >>> d
# {1: 1, 2: 1.23, 3: (1+6j), 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
# >>> d[3] = 4
# >>> d
# {1: 1, 2: 1.23, 3: 4, 4: 'string', 5: [1, 2, 3], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
# >>> d[5] = 10
# >>> d
# {1: 1, 2: 1.23, 3: 4, 4: 'string', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
# >>> d[6] = 12
# >>> d
# {1: 1, 2: 1.23, 3: 4, 4: 'string', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
# >>> d[7] = 20
# >>> d
# {1: 1, 2: 1.23, 3: 4, 4: 'string', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
