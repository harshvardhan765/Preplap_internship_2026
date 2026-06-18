
print("--- Enter Student Details ---")

name = input("Enter Student Name: ")
email = input("Enter Email Address: ")
phone_number = input("Enter Phone Number: ")


age = int(input("Enter Age: "))
marks = float(input("Enter Marks/Percentage: "))

# ******************************************
# PART 2: PRINTING FORMATTED OUTPUT
# ******************************************
print("\n====================================")
print("         STUDENT PROFILE            ")
print("====================================")
print(f"Name         : {name}")
print(f"Age          : {age} years old")
print(f"Marks        : {marks}%")
print(f"Email        : {email}")
print(f"Phone Number : {phone_number}")
print("====================================")