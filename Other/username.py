def __main__():

  # varible inputs - to be used during username creation
  FirstName = input ("What is your first name?")
  LastName = input ("What is your surname?")
  DateJoined= input ("When did you join?")

  # making the varilbes in lowercase
  FirstName=FirstName.lower()
  LastName=LastName.lower()

  # variable to create username variable to be filled.
  username=""
  
__makeUsername__(FirstName, LastName, DateJoined, username)

def __makeUsername__(FirstName, LastName, DateJoined, username):

  #username sorted as part 1 last name
  #Check to see the length of username, if less than 4, add straight in, if over 4, loop for first 4 characters.
    if len(LastName) <= 4 :
      username = username + LastName
  else:
    for i in range (0,4,1):
      username= username + LastName[i]
  
   #Check to see the length of username, if less than 4, add straight in, if over 4, loop for first 4 characters.
  if len(FirstName) <= 4 :
    username = username + FirstName
  else:
    for i in range (0,4,1):
      username = username + FirstName[i]

  #Validation of year is right through a loop
  while len(DateJoined)!= 4:
    print("please enter a 4 digit year")
    DateJoined = input("input year")

  #loop for the last 2 digits so a year is added on the last part
  for i in range (2,4,1):
    username=username + DateJoined[i]
  
  # printing the username out
  print ("Your username is:")
  print (username)

__main__()