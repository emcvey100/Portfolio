#Write a game that:
#-allows the user to play rock,paper,scissors against the computer
#-must display the computer's choice and show the result of the game

import random
# getting varible choices
rps = ["rock","paper","scissors"]
#users idea choice chosen and under that computer chosen
choice= input("Rock, paper or scissors:")
choice= choice.lower()
if choice != "rock" and choice != "paper" and choice != "scissors":
  _choices_(rps, win, lose, draw)
else:
  computer = random.choice(rps)
  print ("You chose", choice,)
  print ("The computer chose", computer)
#see who wins
if choice == "rock" and computer == "scissors"or choice == "paper" and computer == "rock" or choice == "scissors" and computer == "paper":
    print("You win")
elif choice == computer:
    print("You draw")
else:
    print("You lose")
