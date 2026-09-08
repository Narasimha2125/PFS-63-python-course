# # Position argument

# def display(name, email, password):
#     print(f'name: {name}')
#     print(f'email: {email}')
#     print(f'password: {password}')

# display('baireddy', 'baireddy123@gmail.com', 'baireddy@123')
# display('baireddy123@gmail.com', 'baireddy@123', 'biareddy')
# display('baireddy@123', 'baireddy', 'baireddy123@gmail.com')

# # Keyword Argument

# def display(name, email, password):
#     print(f'name: {name}')
#     print(f'email: {email}')
#     print(f'password: {password}')

# display(name='baireddy', email='baireddy123@gmail.com', password='baireddy@123')
# display(email='baireddy123@gmail.com', password='baireddy@123', name='biareddy')
# display(password='baireddy@123', name='baireddy', email='baireddy123@gmail.com')

# # defalut argument

# def display(name, email='gmail.com', password=''):
#     print(f'name: {name}')
#     print(f'email: {email}')
#     print(f'password: {password}')

# display('baireddy', 'baireddy123@gmail.com', 'baireddy@123')
# display('baireddy', 'baireddy123@gmail.com')
# display('baireddy')

# # INVALID LENGTH ARGUMENT POSITION

# def display(*names):
#     print(names)

# display('baireddy')
# display('baireddy', 'narasimha')
# display('baireddy', 'narasimha', 'reddy')
# display('baireddy', 'narasimha', 'reddy', 'garu')

# INVALID LENGTH ARGUMENT KEYWORD

# def display(**products):
#     print(products)

# display(bags=5000)
# display(bags=5000, book=30)
# display(bags=5000, book=30, bottle=300)


