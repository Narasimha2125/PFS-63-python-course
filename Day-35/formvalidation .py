'''
import re
fullname = input("Enter the name: ")
pattern = r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'
res = re.fullmatch(pattern,fullname)
print("Valid full name" if res else "Invalid full name")

import re
fullname = input("Enter the name: ")
pattern = r'^[A-Za-z0-9._]+@[A-Za-z0-9._]+\.[A-Za-z0-9._]{2,}$'
res = re.fullmatch(pattern,fullname)
print("Valid full name" if res else "Invalid full name")

import re
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'
phone_number = input("Enter your phone number: ")
res = re.fullmatch(pattern, phone_number)
print("Valid Phone number" if res else "Invalid Phone number")

import re
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@$!%?&])[A-Za-z0-9@$!%?&]{8,}'
password = input("Enter your password: ")
res = re.fullmatch(pattern, password)
print("Valid password" if res else "Invalid password")

# import re
# username = input('Enter your full name: ')
# pattern = r'^[A-Za-z]{2,25}([A-Za-z]{2,25})+$'
# res = re.fullmatch(pattern, username)
# print("Valid username" if res else "Invalid username")

import re
aadhar = input('Enter your Aadhar number: ')
pattern = r'^[2-9]\d{3} \d{4} \d{4}$'
res = re.fullmatch(pattern, aadhar)
print("Valid Aadhar number" if res else "Invalid Aadhar number")

import re 
pancard = input('Enter the PAN card number: ')
pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
res = re.fullmatch(pattern, pancard)
print('Valid PAN card number' if res else 'Invalid PAN card number')
'''