
# ---------------Error Handling----------------

# try:
#     a = int(input("enter an int value;"))
#     b = int(input("enter an int value;"))
# except ValueError:
#     print("support only integer values")
# #
# #
#
# def get_eligibility_from_class(student_class: int) -> EligibilityStatus:
#     if 3 <= student_class <= 5:
#         return EligibilityStatus.JUNIOR
#     elif 6 <= student_class <= 8:
#         return EligibilityStatus.MIDDLE
#     elif 9 <= student_class <= 10:
#         return EligibilityStatus.SENIOR
#     else:
#         raise HttpError(
#             HTTPStatus.UNPROCESSABLE_ENTITY,
#             "Student class must be between 3 and 10 to determine eligibility.",
#         )
#
