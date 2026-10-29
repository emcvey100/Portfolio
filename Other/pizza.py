import os
def size():
  input()
  os.system("clear")
  baseSize = ["Small", "Medium", "Large"]
  for i in baseSize:
    print (i)
  Size = input("What size do you want:")
  
  Size= Size.capitalize()
  f = 0
  for i in baseSize:
    if Size == i:
      _topping_(Size)
      f=1
  if f == 0:
    print ("Sorry that it has not been found please try again")
    size()
  _topping(size)
  

def _topping_(Size):
  top = "no"
  while top == "yes":
    input()
    os.system("clear")
    Toppings = [
      "pepperoni",
      "Spicy minced beef",
      "Chicken", 
      "Anchovies", 
      "Cajun Chicken", 
      "tuna", 
      "mushrooms", 
      "peppers", 
      "red onions",
        "Jalapenos", 
        "Sweetcorn", 
        "cheese",
        "ham",
        "green chillies"]
    for i in Toppings:
      print (i) 
    uTopping = input("What topping do you want?")
    f = 0
    for i in Toppings:
      if Size == i:
        for i in user:
          if i == user:
            print("You already have this topping!")
          else:
            user = user + uTopping
        f=1
    if f == 0:
      print ("Sorry that it has not been found please try again")
    top = input ("Do you want another topping?").lower()
    top = top.lower

size()