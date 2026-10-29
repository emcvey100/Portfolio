import random
print ("Welcome to the National Lottery!")
start = input("Do you want to start the draw?")
if start == "Yes":
  print(random.randrange(1,59))
elif start == "yes":
  print(random.randrange(1,59))
elif start == "y":
  print(random.randrange(1,59))
else:
  print("Goodbye")