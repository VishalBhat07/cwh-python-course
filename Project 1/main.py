import random

userDict = {
    "Stone": -1,
    "Paper": 0,
    "Scissor": 1
}

comp = -1

while (True):

    choice = int(input("Enter you choice : "))

    if (choice == comp):
        print("Draw")
    elif (choice == -1 and comp == 0):
        print("You lose")
    elif (choice == -1 and comp == 1):
        print("You win")
    elif (choice == 0 and comp == 1):
        print("You lose")
    elif (choice == 0 and comp == -1):
        print("You win")
    elif (choice == 1 and comp == -1):
        print("You lose")
    elif (choice == 1 and comp == 0):
        print("You win")
    else:
        print("Enter a valid choice !!")
