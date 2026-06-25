# numbers = [1, 2, 3]
#
# result = []
#
# for num in numbers:
#     result.append(num * 2)
#
# numbers = [1, 2, 3]
#
# result = list(
#     map(
#         lambda num: num * 2,
#         numbers
#     )
# )
#
# print(result)


#MODULE/TOPIC: Functions..!

#i). Create a function to calculate percentage..!
def calc_prcntage(marks=(12,45,67,86,49)):
    total = sum(marks)
    percentage = total/len(marks)
    return percentage

# Give the marks(Parameter/Arguments) data..!
#m = [12,45,67,86,49]
# Call the calc_prcntage function..!
#print("\nTotal Percentage is: ",calc_prcntage(m))
print("\nTotal Percentage is: ",calc_prcntage())

#ii). Create a function to check pass/fail result..!
def result(marks):
    if marks >= 33:
        return "Congrats! You'r Pass."

    else:
        return "Fail Try Again!"

#m = int(input("\nEnter student obtained marks: "))
#Function calling..!
#print("\nYour result is: ",result(m))
m = 45
print("\n",result(m))

#iii). Create a function to validate mobile number..!
import re
def valid_Nmbr(phNo):
    pattern = r'^[6-9]\d{9}$'

    if re.match(pattern,phNo):
        return "Phone Number is Valid."

    else:
        return "Invalid Phone Number."

# Taking phnmbr from the user..!
phone_nmbr = (input("\nEnter your phone number: "))
#Funcion Calling..!
print(valid_Nmbr(phone_nmbr))


#iv). Create a function to calculate total marks..!
def total_Marks(mark=(12,45,67,86,49)):
    total = sum(mark)
    return total

#Function calling..!
print("\nTotal marks is: ",total_Marks())