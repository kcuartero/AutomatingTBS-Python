#! python3
# created a function using regex for password detection
import re

def strongPassword(password):
    pwRegex = re.compile(r'''(
        (\w{8,})          #length minimum 8 - can be characters or numbers
        (.*[a-z])         #must contain lowercase
        (.*[A-Z])         #must contain uppercase
        (\d)             #must contain at least 1 digit
    )''',re.VERBOSE)

    passwordValidation = pwRegex.search(password)
    if passwordValidation != None:
        return True

password = input("Enter a password: ")
test = strongPassword(password)

if test == True:
    print('Your password is strong')
else:
    print('Your password is not secure enough. Try again')