import random
print ("Welcome to the National Lottery!")
start = input("Do you want to start the draw?")

start=start.lower()
while True:
  print(random.randrange(1,59))
  start = input("Do you want to draw another number?")
  start=start.lower()

print("Goodbye")