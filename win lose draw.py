#start+varibles
NumWon=0
NumLost=0
NumDrew=0
postpone=0
start=input("Welcome to Game counter would you like to input results? y/n")
start=start.lower()
#loop
while start=="yes" or start=="y":
  result=input("How did the game go, did you win, lose or draw?")
  result=result.lower()
  #if won lost or drew
  if result=="win" or result=="won":
    NumWon=NumWon+1
    print("Well done you won!")
  elif result=="lose" or result=="lost":
    NumLost==NumLost+1
    print("Oh well better luck next time!")
  elif result=="draw" or result=="drew":
    NumDrew==NumDrew+1
    print("It is better than losing")
  else:
    postpone=postpone+1
    print("Hope you have another game soon")
  #alble to loop again
  start=input("Would you like to input another result? y/n ")
  start=start.lower()
#ending program to show all results
print("You have won an astonding", NumWon, "games!")
print("Unfortunatly you have lost", NumLost, "games!")
print("You drew", NumDrew, "games!")
print("You postponed", postpone, "games!")
