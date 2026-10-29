def _intro_():
  Name = input("What is you name?")
  Name = Name.capitalize()
  print("Hello", Name + "! ", "You find your self trapped in a red room. You hear a noise it is just a song. You think it is meowing cat because it is so annoying. You have forgotten everything. Your brain hurts so can only ever process two things.")
  _door_()

def _door_():
  print ("You look around and all you see is a door. Do you a: learn how to walk or b: walk over to door?")
  walk = input ("A or B?")
  walk = walk.lower()
  door(walk)

def door(choice):
  if choice == "a":
    print("You chose to learn how to walk. You now know you have some common sense.")
    _buttondoor_()
  elif choice == "b":
    print("You chose to walk. You do not seem very clever.")
    _restwalk_()
  else:
    _error_()

def _restwalk_():
  print ("You tried to walk to the door but fall down and hit your head. Every thing starts to become more blurry. Do you a: try and keep walking or b:rest until feeling better. ")
  choice = input ("A or B?")
  choice = choice.lower()
  restwalk(choice)

def restwalk(choice):
  if choice == "a":
    print("You lose your step no one sees you and you are never seen ever again!")
  elif choice == "b":
    print("You chose to rest and find yourself feeling better.")
    _door_()
  else:
    _error_()

def _buttondoor_():
  print ("It is really strange that their is no one their and then you hear a few footsteps. Do you a: shout for help or b: walk over to the door?")
  walk = input ("A or B?")
  walk = walk.lower()
  buttondoor(walk)
  
def buttondoor(choice):
  if choice == "a":
    print("You try and shout but you can't. So then you take a deep breath and words flow out your mouth. Suddenly, their is a man who come in dressed in white")
    _fightflight_()
  elif choice == "b":
    print("You find a button next to the door.")
    _button_()
  else:
    _error_()



def _fightflight_():
  print ("He is coming closer to you. Do you a: fight him or b: run away?")
  walk = input ("A or B?")
  walk = walk.lower()
  fightfligh(walk)
 

def fightfligh(walk):
  if walk == "a":
    print("You try and knock him out but he is stronger than you. He knocks you out and you wake up not knowing anything.")
    _door_()
  elif walk == "b":
    print("You run out the door for safty.")
    _lr_()
  else:
    _error_()

def _button_():
  print ("You look closer at the . Do you a: press the button or b: you look at the door?")
  walk = input ("A or B?")
  walk = walk.lower()
  fightfligh(walk)

def button(walk):
  if choice == "a":
    print("You find a small handle on the door. It opens. Suddenly, their is a man who come in dressed in white.")
    _fightflight_()
  elif choice == "b":
    print("You find a little handle and push it which opens the door. You run out the door to understand everything.")
    _lr_()
  else:
    _error_()

def _error_():
    print ("sorry error")
    c=input("do you want to start again: y/n")
    c=c.lower()
    if c== "y" or c=="yes":
      _intro_()
    else:
      print ("goodbye")

def _lr_():
  print ("You look around and theirs two paths Do you a: turn right or b: turn left?")
  walk = input ("A or B?")
  walk = walk.lower()
  lr(walk)

def lr(walk):
  if choice == "a":
    print("You look and see a police man.")
    _pm_()
  elif choice == "b":
    print("You find a computer.")
    _comp_()
  else:
    _error_()

def _comp_():
  print ("You walk up to the computer. Do you a: go on the computer on or b: keep walking ?")
  walk = input ("A or B?")
  walk = walk.lower()
  comp(walk)

def comp(walk):
  if choice == "a":
    print("You were never seen again no one ever knew what happened to you.")
  elif choice == "b":
    print("You get hit by something and you forget everything and find yourself back at the start in an empty room.")
    _door_()
  else:
    _error_()

def _pm_():
  print ("You walk closer to him and he is on the phone talking about an arest. Do you a: talk to him or b: run away?")
  walk = input ("A or B?")
  walk = walk.lower()
  pm(walk)

def pm(walk):
  if choice == "a":
    print("You talk to him and he explains that an evil company were trying to turn you into a robot and it was good you escaped as the last test trials died. Later, you found out that you were the next test suject and your spouse at the time had knocked you out and sent you here. You are put in a safe house and live the rest of your life in fear but safe and free.")
    _pm_()
  elif choice == "b":
    print("You run and caught and arrested for the murders of the companies test sujects. You are senteced to life and you plea but it is no use. They do a medical check on you and realise you are not completly human and that the company had put a robot parts to you. You live the rest of your life in prison with evil people looking for you.")
  else:
    _error_()

_intro_()
