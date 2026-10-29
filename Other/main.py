spins=50
daily=1
import random
def _main_():
  # seting varibles
  UserID = []
  PassID = []
  spins=50
  daily=1

 # file handling username and password lists
  with open ("username.txt", "r") as myuser:
    UserID=myuser.readlines()
  with open ("password.txt", "r") as mypass:
    PassID=mypass.readlines()
  print
  #user inputs 
  User = input ("Username:")
  Pass = input ("Password:")
  # linear search for username validation
  found = False
  for i in range(0, len(UserID)):
    if UserID[i] ==User:
      if PassID [i] == Pass:
        found = True
        usernum = i
        print ("Welcome", User, "to Coin Master!" )
      break
  #validation response to area needed
  if found == True:
    _files_(User, usernum, spins, daily)
  else:
    print ("Sorry login details not accepted. Please try again.")
    _main_()

def _files_(User, usernum, spins, daily):
  #opening all files needed with info
  with open ("level.txt", "r") as mylevel:
    level=mylevel.readlines()
    level=level[usernum]
  with open ("house.txt", "r") as myhouse:
    house=myhouse.readlines()
    house=house[usernum]
  with open ("pet.txt", "r") as mypet:
    pet=mypet.readlines()
    pet=pet[usernum]
  with open ("plant.txt", "r") as myplant:
    plant=myplant.readlines()
    plant=plant[usernum]
  with open ("statue.txt", "r") as mystatue:
    statue=mystatue.readlines()
    statue=statue[usernum]
  with open ("transport.txt", "r") as mytransport:
    transport=mytransport.readlines()
    transport=transport[usernum]
  with open ("coins.txt", "r") as mycoins:
    coins=mycoins.readlines() 
    coinlist=coins
    myCoins=coins[usernum]
    #input()
    CM = _coinMaster_(coins, myCoins)
    #print(x)
    #input()
  _village_(level, house, pet, plant, statue, transport, coins,myCoins, User, usernum, spins, daily, CM)

def _coinMaster_(coins, myCoins):
  #bubble sort the coin amount
  for i in range (0, len(coins)):
    coins[i]=int(coins[i])
  num=len(coins) 
  swap = True 
  while num > 0 and swap == True:
    swap = False
    num = num -1
    for i in range (0, num):
      if coins[i] < coins[i+1]:
        temp = coins [i]
        coins [i] = coins [i + 1]
        coins [i+1]=temp
        swap = True
  #print (coins)
  myCoins= int(myCoins)
  if coins[0]==myCoins:
    CM = coins[1]
    #print (CM)
  else:
    CM = coins[0]
    # needs work
  return CM

def _village_(level, house, pet, plant, statue, transport, coins,myCoins, User, usernum,spins, daily, CM):
  print ("You are at ", level, "!")
  print ("You are transport is", transport, "stars!")
  print ("You are house is", house, "stars!")
  print ("You are pet is", pet, "stars!")
  print ("You are plant is", plant, "stars!")
  print ("You are statue is", statue, "stars!")
  print ("You have", myCoins, "coins!")
  #input ("")
  _opition_(level, house, pet, plant, statue, transport, coins,myCoins, User, usernum, spins, daily, CM)

def _opition_(level, house, pet, plant, statue, transport, coins,myCoins, User, usernum, spins, daily, CM):
  input()
  _clear_()
  # asks what they what to do
  print ("You have", myCoins, "coins!")
  options = ["Spin Slots", "Gamble Slots" "Upgrade Village", "Village Details","Daily Upgrade","Exit"]
  useroption = int(input("""What do you want to do you:
    1. spin slots
    2. gamble slots
    3. upgrade village
    4. village details
    5. daily upgrade
    6. exit
    Please enter the number please!"""))
  useroption = useroption


  if useroption == 1:
    _spin_(spins, myCoins, coins, CM)
  elif useroption == 2:
    _gamble_(myCoins)
  elif useroption ==3:
    _upgrage_(myCoins, house, plant, statue, transport, level)
  elif useroption == 4:
    _village_(level, house, pet, plant, statue, transport, coins,myCoins, User, usernum, spins, daily)
  elif useroption == 5:
    _daily_(myCoins, daily)
  elif useroption == 6:
    #need if statment
    print (goodbye)
  else:
    print("Sorry error!")
    _menu_(level, house, pet, plant, statue, transport, coins,myCoins, User, usernum)


def _clear_():
  # clears screen
  import os
  os.system('cls')
  os.system('clear')
  return

def _spin_(spins, myCoins, coins, CM):
  _clear_()
  print("Spin Slots")
  def _main_():
    if spins >0:
      print("sorry no more spin")
      _option_(level, house, pet, plant, statue, transport, coins,myCoins, User, usernum, spins, daily, CM)
    #diffrent opptions in game
    slots = ["coin",
              "bag of coins",
              "raid",
              "attack",
              "spin",
              "sheild"]
    #random.choice
    # this choses the slot and says it
    slotOne = random.choice(slots)
    print (slotOne)
    slotTwo = random.choice(slots)
    print (slotTwo)
    slotThree = random.choice(slots)
    print (slotThree)
    spins = spins - 1
    
    find(slotOne, slotTwo, slotThree,)

  def find( slotOne, slotTwo, slotThree):
    if slotOne == slotTwo == slotThree:
      if slotOne == "raid":
        print ("raid")
      elif slotOne =="attack":
        print("attack")
      elif slotOne =="coin":
        print("coin")
      elif slotOne =="bag of coins":
        print("")
    else:
        print ("Unfortuneatly, you lose!")
  
  _main_()


def _gamble_(myCoins):
  print ("gamble")

def _upgrade_(myCoins, house, plant, statue, transport, level):
  print ("upgrade")

def _daily_(myCoins, daily):
  print ("daily")
_main_()


