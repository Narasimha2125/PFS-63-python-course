class Flipkart:
    products = {'shirts':1000,'handbag':2000,'pants':3000}
    discount = 30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name = name
        self.phone = phone
        self.address = address
        print(f"Hello {self.name}, Welcome to the Flipkart")


    @staticmethod  #helper function
    def displaydiscount():
        print(f"{Flipkart.discount}% is going to provide discount")

Narasimha = Flipkart()
Narasimha.userinfo('avinash',8106686988,'hyd')
Narasimha.display()
Narasimha.displaydiscount()

bharat = Flipkart()
bharat.userinfo('bharat',9925357291,'che')
bharat.display()
bharat.displaydiscount()

ganesh= Flipkart()
ganesh.userinfo('ganesh',6282965272,'ban')
ganesh.display()
ganesh.displaydiscount()