"""
class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and vedio calls")

class whatsappv3(whatsappv2):
    def ststus(self):
        print("You can add the ststus for 24hours")

a = whatsappv1()
a.messaging()

b = whatsappv2()
b.messaging()
b.calls()

c = whatsappv3()
c.ststus()
c.messaging()
c.calls()

class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and vedio calls")

class whatsappv3(whatsappv1,whatsappv2):
    def ststus(self):
        print("You can add the ststus for 24hours")

a = whatsappv1()
a.messaging()

b = whatsappv2()
b.messaging()
b.calls()

c = whatsappv3()
c.ststus()
c.messaging()
c.calls()

class whatsappv1:
    def messaging(self):
        print("You can message")

class whatsappv2(whatsappv1):
    def calls(self):
        print("You can audio and vedio calls")

class whatsappv3(whatsappv1):
    def ststus(self):
        print("You can add the ststus for 24hours")

a = whatsappv1()
a.messaging()

b = whatsappv2()
b.messaging()
b.calls()

c = whatsappv3()
c.ststus()
c.messaging()

class Whatsappv1:

    def messaging(self):
        print("You can send messages")

class Whatsappv2:

    def extramessages(self):
        print("You can emojis, stickers and gifs")

class Whatsappv3(Whatsappv1, Whatsappv2):

    def calls(self):
        print("We can add audio and video calls")

class Whatsappv4(Whatsappv3):
    def status(self):
        print("You can add the status for 24 hours.")


a = Whatsappv1()
a.messaging()

b = Whatsappv2()
b.extramessages()

c = Whatsappv3()
c.calls()
c.messaging()

d = Whatsappv4()
d.status()
d.calls()

# super ex
class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You can make audio and video calls")

class whatsappv3(whatsappv2):
    def status(self):
        super().status()
        print("You can  like and you can add reaction")
a = whatsappv3()
a.status()

class whatsappv1:
    def status(self):
        print("You can add images and videos")

class whatsappv2:
    def status(self):
        
        print("You can add misic and  stickers")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can  like and you can add reaction")
a = whatsappv3()
a.status()
"""