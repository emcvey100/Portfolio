#Write a program that:
#-asks the user to name one of the Olympic Values(Respect, Excellence and Friendship)
#-if they correctly name one, output 'That's correct', otherwise output 'Try again'

#user input their guess
guess = input("Name one of the Olympic Values:")
guess.lower()
#sees if got one correct
if guess == "respect" or guess == "excellence" or guess = "friendship":
    print("That's correct")
else:
    print("Try again")
