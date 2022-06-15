
from asyncio import format_helpers
from random import seed
from random import randint


rock ="    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)\n"
paper="    _______\n---'   ____)____\n          ______)\n          _______)\n         _______)\n---.__________)\n"  #Not my art found at https://www.asciiart.eu/people/body-parts/hand-gestures
scissors="    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)\n"
compWin="=== COMPUTER WINS ===\n"
playerWin="=== PLAYER WINS ===\n"
line="--------------------------------"

seed()


def validate(varA):
    try:
        int(varA)
    except:
        print("That value will not work please try again")
        return False

    if int(varA) > 2 or int(varA) < 0:
        print("That value will not work please try aggain")
        return False
    else:
        return True

def validatePlay(varA):
    try:
        int(varA)
    except:
        print("Goodbye")
        return False

    if int(varA) != 1:
        print("Goodbye")
        return False
    else:
        return True


selections = ["rock", "paper", "scissors"]
art = [rock, paper, scissors]


play = True
playInput = 1

while play == True:
    #setting up game variables
    compPick = randint(0, 2)
    compSelection = selections[compPick]
    userInput = 49
    is_true = False

    #get the user input and display what they picked and what the PC picked
    while is_true != True:
        userInput = input("What would you like to select? (0 - rock, 1 - paper, 2 - scissors)")
        is_true = validate(userInput)
    userPick = int(userInput)
    print(line)
    print("YOU PICKED:")
    print(line)
    print(selections[userPick])
    print(art[userPick])
    print(line)
    print("COMPUTER PICKED:")
    print(line)
    print(selections[compPick])
    print(art[compPick])

    #There is probably a better way to do this, however for this project I am more focused on making sure that my validation works
    if userPick == compPick:
        print("=== TIE ===")
    elif userPick == 0 and compPick == 1:
        print(compWin)
    elif userPick == 0 and compPick == 2:
        print(playerWin)
    elif userPick == 1 and compPick == 0:
        print(playerWin)
    elif userPick == 1 and compPick == 2:
        print(compWin)
    elif userPick == 2 and compPick == 0:
        print(compWin)
    elif userPick == 2 and compPick == 1:
        print(playerWin)
    else:
        print("Something Went Wrong")

    #Find out if the user wants to continue playing
    playInput = input("Press 1 to continue playing: ")
    play = validatePlay(playInput)
    userInput = 49