# RecursionError

# def display(n):
#     if n>10:
#         return
#     print(n)
#     display(n+1)
# display(1)

# def display(n):
#     if n>10:
#         return
#     display(n+1)
#     print(n)
# display(1)

# def displaysum(n):
#     if n==0:
#         return 0
#     return n+displaysum(n-1)
# print(displaysum(10))

# def displayprod(n):
#     if n==1:
#         return 1
#     return n*displayprod(n-1)
# print(displayprod(5))

# s =  'python programming'
# def separate(s, i=0):
#     if i == len(s):
#         return
#     if s[i] == ' ':
#         print("First word:", s[:i])
#         print("second word:", s[i+1:])
#         return
#     separate(s, i+1)
# separate(s)

# def display(ind):
#     if ind == len(s):
#         return
#     print(s[ind],end='')
#     display(ind+1)

# s =  'python programming'
# display(0)

# s = 'Baireddy'

# def display(s, ind=0):
#     if ind == len(s):
#         return
#     print(s[:ind + 1])
#     display(s, ind +1)

# display(s)

# s = "python"

# def display(s, i=0):
#     if i + 3 > len(s):
#         return

#     print(s[i:i+3])
#     display(s, i+1)

# display(s)

# n = 987654
# def display(n):
#     if n == 0:
#         return
#     display(n//10)
#     print(n%10)
# display(n)

# def display(n):
#     if n == 0:
#         return
#     display(n//10)
#     print(n%10)
# display(n)

# def display(n):
#     if n == 0:
#         return 
#     return display(n//10)
#     print(n%10)
# display(n)