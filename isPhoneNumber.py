def isPhoneNumber(text):
    if len(text) != 12: # if text is not 12 characters long, return False
        return False
    for i in range(0,3):  #from the first 3 digits
        if not text[i].isdecimal(): # if not a number, return False
            return False
    if text[3] != '-': #if the 4th character is not a "-" , return False
        return False
    for i in range(4,7): #from 4 to 7
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
