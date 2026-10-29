print('''
    ___
    ).x)
   (:_(

     V       V       V       V
    / \     / \     / \     / \       
   / $ \   / $ \   / $ \   / $ \      
  (_____) (_____) (_____) (_____)
       ''')
print("Welcome to treasure island. Your mission is to find the treasure.")
option= input("There are two paths one right and one left. Do you go left or right?:")
if option.lower() == "left":
    option = input("The tide across the river is high. Do you wait for it to go or do you swim across?:")
    if option.lower() == "wait":
        option=input("You successfully cross and find 3 doors, a yellow a blue and a red one. Which do you choose?:")
        if option.lower() == "red":
            print("You were burned by a fire. \n Game Over.")
        elif option.lower() == "blue":
            print("You were eaten by beasts. \n Game Over.")
        elif option.lower() == "yellow":
            print("You found the treasure. \n You win!")
        else:
            print("Game over")
    else:
        print("You were attacked by trout. \n Game Over.")
else:
    print("You fell in a hole. \n Game over.")
    
