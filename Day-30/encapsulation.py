# class Instagram:
#     def __init__(self,username,password):
#         self.username = username
#         self.__password = password
#         self._posts = []

#     def getpassword(self):
#         return self.__password

#     @property
#     def accesspost(self):
#         return self._posts

#     def display(self):
#         print(self.username,self.__password,self._posts)

# Narasimha = Instagram('Narasimha', 'Narasimha@123')
# Narasimha.display()
# print(Narasimha.username)
# print(Narasimha.getpassword())
# print(Narasimha.accesspost)


class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._posts = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpasword):
        self.__password = newpasword

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)

    def display(self):
        print(self.username,self.__password,self._posts)

Narasimha = Instagram('Narasimha', 'Narasimha@123')
Narasimha.display()
print(Narasimha.username)
print(Narasimha.getpassword())
print(Narasimha.accesspost)

Narasimha.username = 'Baireddy'
Narasimha.setpassword('Baireddy@123')
Narasimha.accesspost = "sunrise.png"
Narasimha.accesspost = "forest.png"
Narasimha.accesspost = "mountaion.png"

print(Narasimha.username)
print(Narasimha.getpassword())
print(Narasimha.accesspost)