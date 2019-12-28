# Author      : Isaiah Jared
# Description : Simple CLI-based Rock-Paper-Scissors
#               game.

import random
import os
import sys

userOS = str(sys.platform)

# Used to avoid visual clutter for the user in the command line 
def clearFunc():
  if "win32" not in userOS:
    os.system('clear')
  else:
    os.system('cls')

def main():

  running = True

  while running == True: # MAIN GAME LOOP

    clearFunc()
    oppChoiceList = ['1','2','3']
    oppChoice = random.choice(oppChoiceList)

    print("Welcome to Rock-Paper-Scissors!")
    print("\nPlease select an option from the list below (use 1-3): \n1. Rock\n2. Paper\n3. Scissors\n")

    userInput = input()

    if userInput == '1':
      if oppChoice == '1':
        print("You picked: Rock\nComputer picked: Rock\n\nYou Tied!")
        
      elif oppChoice == '2':
        print("You picked: Rock\nComputer picked: Paper\n\nComputer Wins!")
        
      elif oppChoice == '3':
        print("You picked: Rock\nComputer picked: Paper\n\nYou Win!")
        
      else:
        print("Something broke :^)")
        

    elif userInput == '2':
      if oppChoice == '1':
        print("You picked: Paper\nComputer picked: Rock\n\n You Win!")
        
      elif oppChoice == '2':
        print("You picked: Paper\nComputer picked: Paper\n\nYou Tied!")
        
      elif oppChoice == '3':
        print("You picked: Paper\nComputer picked: Scissors\n\nComputer Wins!")
        
      else:
        print("Something broke :^)")
        

    elif userInput == '3':
      if oppChoice == '1':
        print("You picked: Scissors\nComputer picked: Rock\n\nComputer Wins!")
        
      elif oppChoice == '2':
        print("You picked: Scissors\n Computer picked: Paper\n\nYou Win!")
        
      elif oppChoice == '3':
        print("You picked: Scissors\nComputer picked: Scissors\n\nYou Tied!")
        
      else:
        print("Something broke :^)")
        
    else:
      print("Invalid input!")
      
    playAgain = input("Would you like to play again? (enter Y/N): ").lower()
    
    while playAgain not in ("y", "n"):  
      print("Invalid input!")
      playAgain = input("Would you like to play again? (enter Y/N): ")
    if playAgain == "n":
      running = False

main()
