coin = "yes"
import os
import random
while coin == "yes":

    toss = ['Heads' , 'Tails' ]
    
    do = random.choice(toss)
    print("You Got : ")
    print(do)
    
    print ("\nType yes or y to Toss the coin again...!!!")
    coin = coin.lower()
    
    if coin == "y":
        coin = "yes"
os._exit
