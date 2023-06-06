import random
def roll():
  print(random.randint(1,6))
  choice=input("Do you want to play again? Y/N:").lower()
  if choice=="y" or choice=="yes":
    roll()
roll()