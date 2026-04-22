import re

# Email validation function
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)


# Phone validation function (10-digit Indian number)
def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    return re.match(pattern, phone)


# Input
email = input("Enter email: ")
phone = input("Enter phone number: ")

# Output
if validate_email(email):
    print("Valid Email")
else:
    print("Invalid Email")

if validate_phone(phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
