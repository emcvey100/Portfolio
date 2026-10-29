def __main__():
  #welcomes in the program 
  print("Welcome to the area volume maker for cuboid and retangles.")
  _area_()

def _area_():
  #varibles to keep so we can find areas
  h=float(input("What height is the box in cm?"))
  w=float(input("What width is the box in cm?"))
  l=float(input("What length is the box in cm? If only area put a 0"))
  #asks if 
  if l!=0:
    ans=h * w
    print("Your area is", ans)
    ans=ans *l
    print ("Your volume is", ans)
    __loop__()
  else:
    ans=h * w
    print("Your area is", ans)
    __loop__()

def __loop__():
  again= input("Do you want to put another area? y/n")
  again = again.lower()
  if again == "y" or again == "yes":
    _area_()
  else:
    print("Goodbye! Thankyou for using this program.")

__main__()