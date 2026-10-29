import random
def _main_():
    #diffrent opptions in game
    slots = ["coin",
              "7",
              "dimond",
              "cherry",
              "bar",
              "bell",
              "oranges"]
    #random.choice
    # this choses the slot and says it
    slotOne = random.choice(slots)
    print (slotOne)
    slotTwo = random.choice(slots)
    print (slotTwo)
    slotThree = random.choice(slots)
    print (slotThree)
    
    find(slotOne, slotTwo, slotThree,)

def find( slotOne, slotTwo, slotThree):
    if slotOne == slotTwo == slotThree:
        print ("You win")
    else:
        print ("Unfortuneatly, you lose!")

_main_()
