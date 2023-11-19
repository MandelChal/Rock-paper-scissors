import sys
import random
from enum import Enum

again = True
class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
   
while(again):
    print("")
    playerChoice = input("Enter...\n1 for Rock \n2 for Paper \n3 for Scissors \n\n")
    computerChoice = random.choice("123")

    player = int(playerChoice)
    if (player < 1 or player > 3):
        sys.exit("You must enter 1, 2, or 3.\n")

    computer = int(computerChoice)
    print("Your choice is: " + str(RPS(player)).replace('RPS.','') + ".")
    print("Python's choice is: " + str(RPS(computer)).replace('RPS.','') + ".\n")

    if (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win! 🏆\n")

    elif (player == computer):    
        print("Tie game! 🪢\n")

    else:
        print("Python wins! 👻\n")

    newGame = input("Play again? \nY for Yes  \nQ to Quit  \n\n")
    if newGame.lower() == 'y':
        continue
    
    else:
        print("\n🎉🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        again == False
        sys.exit("Bye! 👏\n")
