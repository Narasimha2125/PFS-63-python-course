# # 1. Single Inheritance – One child class inherits from one parent class.
# #   ex : A → B

# # 2. Multiple Inheritance – One child class inherits from two or more parent classes.
# #     ex : A + B → C

# # 3. Multilevel Inheritance – A class inherits from another derived class, forming a chain.
# #     ex : A → B → C

# # 4. Hierarchical Inheritance – Multiple child classes inherit from the same parent class.
# #     ex : A → B, C, D

# # 5. Hybrid Inheritance – A combination of two or more inheritance types, such as multiple and hierarchical inheritance.


# class whatsappV1:
#     def __init__(self,name):
#         self.name = name
#         print(f"Welocome to whatsapp - v1 {self}!")
#     def messaging(self):
#         print("Yo can send messages")

# class whatsappv2(whatsappV1):
#     def __init__(self, name):
#         self.name = name
#         print(f"Welcome to the whatsapp - V2 {self.name}!")
#     def calls(self):
#         print("You can have audio and vedio calls")

# Narasimha = whatsappV1('Narasimha')
# Narasimha.messaging()

# Baireddy = whatsappv2('Baireddy')
# Baireddy.messaging()
# Baireddy.calls()
