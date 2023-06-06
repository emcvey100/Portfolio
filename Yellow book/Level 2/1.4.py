import random
number= random.randint(1,20)
guess=0
trys=0
while trys<20:
  guess=int(input("Please enter an interger:"))
  if number < guess:
    print("Your guess is too high")
  elif number > guess:
    print("Your guess is too low")
  else:
    break
  trys= trys+1
if trys<=5:
  print("Well done, you are genus")
elif trys<=10:
  print("Well done good work")
elif trys<=15:
  print("Well done, you finally got it")
elif trys<20:
  print("OK you have done it")
else:
  print("I am bored! good luck next time!")