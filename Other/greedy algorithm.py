change =-1
while change < 0:
  price=float(input("What is the price of the item?:"))
  note=float(input("What is the money given?:"))
  change= note - price
noteChoice=[50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.01]
coins=0
coin= "You have " 
for i in noteChoice:
    coins= coins + (change // i)
    if (change // i) > 0:
        coin= coin + str(int((change // i))) + "x £" + str(i) + "  "
    change= round(change%i,2)
print ("You have " + str(int(coins)) + " change")
print(coin)
