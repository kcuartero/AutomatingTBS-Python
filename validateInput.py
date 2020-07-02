#demo of using isX string methods to validate age and a password

while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal(): #input must be numbers only
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum(): #input must be letters or numbers
        break
    print('Passwords can only have letters and numbers.')
