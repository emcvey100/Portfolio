import random
def _main_():
  # getting varible choices
  rps = [
          "rock",
          "paper",
          "scissors"
          ]
  # VARIBLES TO USE IN THE Future
  win = 0
  lose = 0
  draw = 0
  #welcome
  print ("Welcome to rock paper scissors")
  _choices_(rps, win, lose, draw)

def _choices_(rps, win, lose, draw):
  #users idea choice chosen and under that computer chosen
  choice= input("Rock, paper or scissors:")
  choice= choice.lower()
  if choice != "rock" and choice != "paper" and choice != "scissors":
    _choices_(rps, win, lose, draw)
  else:
    computer = random.choice(rps)
    print ("You chose", choice,)
    print ("The computer chose", computer)
    _if_(choice, win, lose, draw, computer, rps)

def _if_(choice, win, lose, draw, computer, rps):
  if choice == "rock" and computer == "scissors":
    win = win +1
    _loop_(win, lose, draw, rps)
  elif choice =="scissors" and computer == "rock":
    lose = lose + 1
    _loop_(win, lose, draw, rps)
  
  elif choice =="paper" and computer == "rock":
    lose = win + 1
    _loop_(win, lose, draw, rps)

  elif choice =="rock" and computer == "paper":
    lose = lose + 1
    _loop_(win, lose, draw, rps)

  elif choice =="scissors" and computer == "paper":
    lose = win + 1
    _loop_(win, lose, draw, rps)

  elif computer =="scissors" and choice == "paper":
    lose = lose + 1
    _loop_(win, lose, draw, rps)

  else:
    draw = draw +1
    _loop_(win, lose, draw, rps)

def _loop_(win, lose, draw, rps):
  print("Won:", win)
  print("lost:", lose)
  print("draw:", draw)
  loop = input("Do you want another game? y/n")
  loop = loop.lower()
  if loop == "y" or loop == "yes":
    _choices_(rps, win, lose, draw)
  else:
    print ("You won", win, "games.")
    print ("You lost", lose, "games.")
    print ("You drew", draw, "games.")
    print ("Goodbye")

_main_()