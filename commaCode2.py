#example list to test program
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
colors = ['red', 'blue', 'black', 'pink', 'yellow']
def commaCode(myList):
    s= '' # empty variable
    lastValue = myList[len(myList) - 1] # gets last value of the list
    length = int(len(myList)) - 1 #gets length of list
    newList = myList[0:length] #creates new list without last value
    for words in newList:
        s += words + ', '
    print(s + 'and ' + lastValue)

commaCode(colors)
    