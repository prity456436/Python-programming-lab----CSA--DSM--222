import re

def check_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    
    if re.match(pattern, password):
        print("Strong Password")
    else:
        print("Weak Password")


# Input
pwd = input("Enter password: ")
check_password(pwd)
