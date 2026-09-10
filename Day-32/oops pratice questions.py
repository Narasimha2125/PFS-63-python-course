class User:
    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def register(self):
        if self.name == "":
            print("Registration Failed: Name is required")
        elif self.email == "":
            print("Registration Failed: Email is required")
        elif self.phone == "":
            print("Registration Failed: Phone number is required")
        elif self.password == "":
            print("Registration Failed: Password is required")
        else:
            print("Registration Successful")


user = User("Narsimha", "narasimha@gmail.com", 9876543210, "Narasimha@123")
user.register()