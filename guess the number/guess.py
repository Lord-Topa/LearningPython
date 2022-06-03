
from random import seed
from random import randint

seed()
number = randint(0, 100)

def checkInput(varA):
    varB = int(varA)
    if varB == number:
        return 1
    elif varB > number:
        return 0
    else:
        return -1

operate = 0
while operate != 1:
    userInput = input("Enter your guess")
    operate = checkInput(userInput)
    match operate:
        case -1: print("That number is too small")
        case 0: print("That number is too large")
        case 1: print("That is the correct number")
                