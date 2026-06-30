

# ---------------- Day~11 -------------------- .
#
# #MODULE/TOPIC: Regular Expression (Regex)..!
#
# #1). Create validation function for email..!
# import re
# def validate_email (email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#
#     if re.fullmatch(pattern,email):
#         return "Valid Email."
#
#     else:
#         return "Invalid Email."
#
# email = input("Please! Enter your Email: ")
# print(validate_email(email))

#2). Create validation function for Indian Mobile Number..!
# import re
# def validate_mobile(number):
#     pattern = r'^[6-9]\d{9}$'
#
#     if re.fullmatch(pattern,number):
#         return "Valid Mobile Number."
#
#     else:
#         return "Invalid Mobile Number."
#
# mobile_Nmbr = input("Enter your mobile number: ").strip()
# print(validate_mobile(mobile_Nmbr))


#3). Create Password Strength Validation..!
import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$'

    if re.fullmatch(pattern, password):
        return "Strong Password"
    else:
        return "Weak Password"

password = input("Enter Password: ")
print(validate_password(password))


#4). Create username format validation..!
import re

def validate_username(username):
    pattern = r'^[A-Za-z][A-Za-z0-9_]{4,14}$'

    if re.fullmatch(pattern, username):
        return "Valid Username"
    else:
        return "Invalid Username"

username = input("Enter Username: ")
print(validate_username(username))