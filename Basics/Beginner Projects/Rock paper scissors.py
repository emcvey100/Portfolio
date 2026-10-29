import random
rock = '''
     _________
_____)   _____)
          ( __)
          ( __)
_____     ( __)
     )____(___)
'''
paper = '''
     _________
_____)   _____)__
           ______)
           ________)
_____      ______)
     )_________)
'''
scissors = '''
     ________
_____)   ( __)____
           _______)
           ________)
_____     ( __)
     )____(___)
'''



choice = input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors. \n")
print("You choose:")
if choice == "0":
    print("Rock \n", rock)
elif choice == "1":
    print("Paper \n", paper)
elif choice == "2":
    print("Scissors \n", scissors)
else:
    print("invalid option")
    exit()
choice = int(choice) #known that code works
computer_choice = random.randint(0, 2)
print("You computer chooses:")
if computer_choice == 0:
    print("Rock \n", rock)
elif computer_choice == 1:
    print("Paper \n", paper)
elif computer_choice == 2:
    print("Scissors \n", scissors)
if computer_choice == choice:
    print("You draw")
elif choice == (computer_choice+1):
    print("You win")
elif computer_choice == (choice+1):
    print("You lose")
elif computer_choice > choice:
    print("You win")
else:
    print("You lose")
