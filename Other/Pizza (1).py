def size():
  baseSize = ["Small", "Medium", "Large"]
  for i in baseSize:
    print (i)
  Size = input("What size do you want:")
  baseSize = baseSize.lower()
  Size= size.lower()
  f = 0
  for i in baseSize:
    if Size == i:
      _topping_(Size)
      f=1
  if f == 0:
    print ("Sorry that it has not been found please try again")
    size()
  _topping(size)
  

def _topping_(size):
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
  uTopping = input("What topping do you want?")
  #if uTopping == 
  top = input ("Do you want another topping?").lower()
  while top == "no":
    top = input ("Do you want another topping?").lower()
    uTopping = input("What topping do you want?")
  
  for i in range (0, len(uTopping)):
      print()
size()