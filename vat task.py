#Intro plus ask start into lower
print("Welcome to the VAT maker.")
Begin = input("Would you like to use the VAT maker?")
Begin = Begin.lower()
#loop it to do it again
while Begin == "yes" or Begin == "y":
  #varibles input price and Item
  Item=input("What Item do you want to find VAT on?")
  print("What price do you want price do you want", Item, "to be?")
  PriceExVat=input()
  #turn into number then VAT
  PriceExVat=float(PriceExVat)
  PriceIntVat=PriceExVat*1.2
  #Printing VAT
  print("Your", Item, "Without Vat is", PriceExVat, "but with Vat it is", PriceIntVat)
  #Would you like to do again
  Begin = input("Would you like to use the VAT maker again?")
  Begin = Begin.lower()
print ("Thankyou for using VAT maker today.")