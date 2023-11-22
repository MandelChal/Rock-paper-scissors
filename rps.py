import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
   
def rps_func():
    print("")
    playerChoice = input("Enter...\n1 for Rock \n2 for Paper \n3 for Scissors \n\n")
    computerChoice = random.choice("123")
    if playerChoice not in ["1","2","3"]:
        print("You must enter 1, 2, or 3.\n")
        return rps_func()
    plyer=int(playerChoice)
    computer = int(computerChoice)
    print("Your choice is: " + str(RPS(plyer)).replace('RPS.','') + ".")
    print("Python's choice is: " + str(RPS(computer)).replace('RPS.','') + ".\n")

    if (plyer == 1 and computer == 3) or (plyer == 2 and computer == 1) or (plyer == 3 and computer == 2):
        print("You win! 🏆\n")

    elif (plyer == computer):    
        print("Tie game! 🪢\n")

    else:
        print("Python wins! 👻\n")

    while True:
        print("Play again?")
        newGame = input( "\nY for Yes  \nQ to Quit  \n\n")
        if newGame.lower() not in ["y","q"]:
            continue
        else:
            break
    if newGame.lower()=='y':
        rps_func()

    else:
        print("\n🎉🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👏\n")

rps_func()        

