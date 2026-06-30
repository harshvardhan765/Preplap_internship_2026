# - Write a program to print name, age,
# course name, and training batch
# name = input("Enter your name: ")
# age  = input("Enter your age: ")
# address = input("Enter your address: ")
from ast import comprehension

# print("name",name)
# print("age",age)
# print("address",address)

# name = "david"
# age = 21
# marks = 3.14
# # bool = True
# #
# # None
#
# print("name",type(name))
# print("age",type(age))
# # print("address",type(address))

# day 2



# # type convergent

# string to int
# age_str ="21"
# age_int = int(age_str)
# # print(type(age_int))



# convert int to float
# marks_int = 90
# marks_float =  float(marks_int)



# Converting a number to a string
# distance = 15
# message = "The gym is " + str(distance) + " miles away."
# print(message)
#
# name = input("Enter your name: ")
# score = 100
# # print(f" {name} score is {score}")
#
# name = input("Enter your name: ")
# department = input("Enter your department: ")
# section = input("Enter your section: ")
# year = input("Enter your year: ")
#
#
# print(f"{name} is the section {section} student on the {department} department in {year} year")

# print formated output


# day 4
#
# l1 = ["david",21 ,21.3]
# print(type(l1),list(l1))
#
# students = [ "david","avi","mayank","vaibhav","mridul","harsh"]
# print(type(students),students)
# list indexing
# print(students[0])
# print(students[1])
# print(students[2])

# list slicing

# numbers = [0,1,2,3,4,5,6,7,8,9,10]
# # Extract index 1 up to (but not including) index 4
# print(numbers[1:4])
#
# # Slice from the beginning to index 3
# print(numbers[:3])
#
# l1= [1,2,3,]
# l2  = [5,6,7]
# print(l1+l2)
# print(l1*3)


# todo = ["clean", "code"]
# todo.append("read")       # ['clean', 'code', 'read']
# # todo.insert(1, "exercise") # ['clean', 'exercise', 'code', 'read']

#
# items = ["david", "laptop", "keys", "phone"]
#
# items.remove("laptop")
# items.remove("keys")
# print(items)
# popped_items = items.pop(0)
# print(items)


# scores = [45, 100, 12, 89]
#
# scores.sort()
# print(scores)  # Output: [12, 45, 89, 100]
#
# scores.reverse()
# print(scores)  # Output: [100, 89, 45, 12]


# creating a tupple
# coordinates = (40.7128,-74.344443)
# print(coordinates[0])


# day 5
# starting to creatin a dictionary
#
# user = {
#     "username": "admin",
#     "password": "david@localhost",
#     "email": "david@gmai.com"
#
# }

# # dictionary copy
# orgin = {"a":1}
# cloned = orgin
#
# cloned["a"] = 99
# print(orgin["a"])
# print(cloned)


# list comprehension
#
# def user_name():
#     print("Enter your name: ")
# user_name()


def student(name):
    print(f"welcome master {name}")
student("harsh")

