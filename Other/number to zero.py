#Task - Play through the game several times to see what it does - see if it breaks anywhere and how

#Task - comment through each section of the code explaining what it does

#Task - Edit code to make the validation more robust.

#Extension - add in code that decides who goes first and then alter the code to allow this to happen.

#Extra Extension - Try and make it so the computer tries to win!!

import random
import sys
# imported all comments needed

def __main__():
  #welcoming into game
  print("Welcome to the game. The objective is to get the OTHER player to land on 0.")
  #asks if you want to start game and keeps the awnser
  startGame = input("Are you ready to start the game? yes/no")
#seeing if it is an awnser so no errors
  while startGame != "yes" and startGame != "no":
    print("The game did not recognise your input, try again")
    startGame = input("Are you ready to start the game? yes/no")
    #below sees if anser is yes so if it is then start game if no then end game
  if startGame == "yes":
    __game__()
  else:
    print("Oh ok, nevermind, bye!")
    sys.exit()

def __game__():
  # computer finds a random number between 20 and 31
  startingNumber = random.randrange(20,31)
  print("The starting number is:" , startingNumber)
  #loop around user and computer's turn until it gets to 0
  while startingNumber > 0 :
    startingNumber = __userturn__(startingNumber)
    startingNumber =__compturn__(startingNumber)


def __userturn__(startingNumber):
  #user inputs number and takes away if less 3 but bigger than 0
  usernum = float(input("Choose 1-3 to remove"))
  # if not in numbers asks again
  while usernum > 3 or usernum < 1:
    print("invalid choice, you must choose between 1-3")
    usernum = float(input("Choose 1-3 to remove"))
  startingNumber = startingNumber - usernum
#  print(startingNumber)
#round the float to whole number
  startingNumber = round(startingNumber,0)
 # print(startingNumber)
  #input()
# turns starting number into interger
  startingNumber = int(startingNumber)
 # print(startingNumber)
  #input()
  #checking number is so small
  while startingNumber < 0:
    print("The number you tried to take away puts your number below zero, try again.")
    startingNumber = startingNumber + usernum
    usernum = float(input("Choose 1-3 to remove"))
    startingNumber = startingNumber - usernum
    #  print(startingNumber)
#round the float to whole number
  startingNumber = round(startingNumber,0)
 # print(startingNumber)
  #input()
# turns starting number into interger
  startingNumber = int(startingNumber)
 # print(startingNumber)
  #input()
 # says if you lose as is 0
  if startingNumber == 0:
    print("0 Left! You lose!")
    sys.exit()
  print(startingNumber, "left")
  # goes back to the start of other bit
  return startingNumber

def __compturn__(startingNumber):
  #computer choses number
    compnum = random.randrange(1,4)
    # computer takes away from the scorre before
    startingNumber = startingNumber - compnum
    #see if it was more before
    while startingNumber < 0:
      startingNumber = startingNumber + compnum
      compnum = random.randrange(1,4)
      startingNumber = startingNumber - compnum 
      # sees if it is equal to zero
    if startingNumber == 0:      
      print("Computer leaves 0 Left! You win!")
      sys.exit()
    print("Computer removes",compnum)
    print(startingNumber, "left")
    return startingNumber

__main__()