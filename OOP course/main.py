from room import Room
from character import Enemy
from character import Freind
from item import Item
backpack=[]
kitchen=Room('Kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("ARRR BRAINS!")
dave.set_weakness("cheese")
dave.set_intrest("pens")
dining_hall.set_character(dave)


jenna=Freind("Jenna", "A freindly ghost")
jenna.set_conversation("Helloooo!")
kitchen.set_character(jenna)

cheese = Item()
cheese.set_name("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

pens = Item()
pens.set_name("pens")
pens.set_description("A multicoloured sharp tiped pen.")
dining_hall.set_item(pens)

money = Item()
money.set_name("money")
money.set_description("A large sum of money that you could do alot with.")
kitchen.set_item(money)

sword = Item()
sword.set_name("sword")
sword.set_description("A sharp shiny sword.")
kitchen.set_item(money)

health=10

current_room = kitchen

dead=False

while dead==False:		
    print("\n")         
    current_room.get_details()
    inhabitant = current_room.get_character()
    item = current_room.get_item()
    if inhabitant is not None:
        inhabitant.describe()
    if item is not None:
        item.describe()
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command =="talk":
        inhabitant.talk()
    elif command == "fight":
        print("what will you fight with?")
        fight_with = input()
        if fight_with in backpack:
            if inhabitant.fight(fight_with)==True:
                health+=3
            else:
                health+=-10
        else:
            print("You don't have the item!")
            health+=-1
    elif command == "bribe":
        print("what will you bribe with?")
        bribe_with = input()
        if bribe_with in backpack:
            if inhabitant.bribe(bribe_with)==False:
                health+=-1
        else:
            print("You don't have the item!")
            health+=-2
    elif command == "steal":
        if inhabitant == None:
          print("No one is here!")
        else:
          if isinstance(inhabitant, Freind):
            print("WHY??????")
          else:
            inhabitant.steal()
        health+=1
    elif command == "hug":
        if inhabitant == None:
          print("No one here")
        else:
          if isinstance(inhabitant, Enemy):
            print("No way your doing that!")
          else:
            inhabitant.hug()
            health+=2
    elif command == "gift":
        if inhabitant == None:
          print("No one here!")
        else:
          if isinstance(inhabitant, Enemy):
            print("WHY??")
          else:
            health+=1
            inhabitant.gift()
    elif command == "take":
        if item == None:
            print("There's no item here!")
        else:
            backpack.append(item.get_name())
            current_room.set_item(None)
    elif command == "check":
        for backpackitem in backpack:
            print(backpackitem)
    elif command == "health":
        print(health)
    if health <= 0:
        dead = True
    elif health >= 100:
        dead = False
if health <= 0:
            print("Oh dear your health is too low.")
            print("You died!")
            dead = True
else:
    print("Well done you won!")
    print("You collected:")
    for i in backpack:
        print(i)
    print("You fend off all the monsters as got health back to 100%")
