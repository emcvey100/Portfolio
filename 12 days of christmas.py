Days = ["1st", "2nd", "3rd", "4th","5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]
Gifts = ["a Partridge in a pear tree", "2 turtle doves and", "3 French Hens", "4 calling birds", "5 Golden rings", "6 geese a lying", "7 swans a swimming", "8 maids a milking", "9 ladies Dancing", "10 lords are leaping", "11 pipers piping", "12 drummers drumming"]
#varibles saying all info in the song above.
sorp = ""
loop = False
while loop == False:
  if sorp == "s":
    #if the customer said s
    loop = True
    # does not carry loop on
    for i in range (0,12):
      print ("On the", Days[i], " day of Christmas, my true love sent to me")
      for x in range(i,-1,-1):
        print (Gifts[x])
      #above plays song using varible and less data
  elif sorp == "p":
    #if the customer said p
    loop = True
    i = 33
    #stops loop
    while i >=12:
      i = int(input("What day do you want presents for?"))
      i = i -1
    #asks what dayuntil in the 12 days
    print ("On the", Days[i], " day of Christmas, my true love sent to me")
    for x in range(i,-1,-1):
      print (Gifts[x])
    #above plays the song
  else:
    # did not comply so asked question
    sorp=input("Do you want song or day with list of presents? p/s")