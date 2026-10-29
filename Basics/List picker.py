#Write a random name generator that asks for the user to input 5 names, stores them in an array and then outputs one of them at random.
import random
names=[]
for in in range(5):
    names.append(input("Name:"))
print(random.choice(names))
