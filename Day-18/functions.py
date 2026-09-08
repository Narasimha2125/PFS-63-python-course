
# def display(name, email, password):
#     print(f'Hello {name},')
#     print(f'Your email {email},')
#     print(f'Your password {password},')

# display('Baireddy', 'baireddy@gmail.com', 'baireddy@123')
# display('Narasimha', 'narasimha@gmail.com', 'narasimha@123')
# display('Reddy', 'reddy@gmail.com', 'reddy@123')


# def isleapyear(year):
#     if year%400 == 0 or (year%4==0 and year%100!=0):
#         print(f'{year} is a leap year')
#     else:
#         print(f'{year} is not a leap year')

# for year in range(1950, 2027):
#     isleapyear(year)


# def sumofdights(n):
#     sum = 0
#     while n>0:
#         sum += n%10
#         n=n//10
#     return sum

# n = int(input("Enter the number: "))
# print(f'sum of {n} digits is {sumofdights(n)}') 


# def productofdights(n):
#     product = 1
#     while n>0:
#         product *= n%10
#         n=n//10
#     return product

# n = int(input("Enter the number: "))
# print(f'product of {n} digits is {productofdights(n)}')  


# def checkpassword(password):
#     if len(password) > 0:
#         check = set()
#         for i in password():
#             if i.isupper():
#                 check.add('u')
#             elif i.islower():
#                 check.add('l')
#             elif i.isdigit():
#                 check.add('d')
#             else:
#                 check.add('s')
#         if len(check) == 4:
#             return "Strong password"
#     return ("weak password")
# password = input("Enter the password")
# print(f' password is{checkpassword(password)}')


