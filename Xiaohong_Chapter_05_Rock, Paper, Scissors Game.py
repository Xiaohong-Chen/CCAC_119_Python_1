import random

computerChoise = random.randint(1,3)
userInput = input("Entering your number choise of 1= rock,2 = paper,3 = scissor:")

def displayComputerChoise():
    if computerChoise==1:
        print("Computer has chosen rock")
    elif computerChoise==2:
        print("Computer has chosen paper")
    else:
        print("Computer has chosen scissors")

def checkWinner():

    if int(userInput)==computerChoise:
        print("You have chosen the same choise with Computer.")
    elif int(userInput) == 1:
        if computerChoise == 2:
            print("Computer Win")
        else:
            print("You Win")
    elif int(userInput) == 2:
        if computerChoise == 3:
            print("Computer Win")
        else:
            print("You Win")
    else:
        if computerChoise == 1:
            print("Computer Win")
        else:
            print("You Win")


def main():
    displayComputerChoise()
    checkWinner()

main()