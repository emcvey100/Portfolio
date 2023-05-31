import random
import time
import datetime

def __main__():
  # Says hello to this menu
  print("""Hello welcome to the menu!""")
  __menu__()

def _clear_():
  # clears screen
  input()
  import os
  os.system('cls')
  os.system('clear')
  return

def __menu__():
  _clear_()
  print(""" What do you want select:
        1) Name varible
        2) Animal chooser
        3) 12 Days of Christmas
        4) Magic 8 Ball
        5) Vat calculator
        6) Win Lose finder
        7) Clock
        8) Hello language
        9) pet suvay
        10) kg to lb
        11) lottery
        12) A lone room (Gamebook)
        13) lotto
        14) calculator
        15) fruit
        16) Joke
        17) Username maker
        18) Coin flip
        19) volume area
        20) miles per hour
        21) time lived
        22) rock paper
        23) Card Game
        24) Slots""")
  choice = int(input("What number will you pick? 1-24"))
  __choice__(choice)

def __choice__(choice):
  if choice ==1:
    _NameVarible_()
  elif choice==2:
    _AnimalChooser_()
  elif choice == 3:
    _Christmas_()
  elif choice==4:
    _Magic8Ball_()
  elif choice ==5:
    _VatCalculator_()
  elif choice == 6:
    _WinLoseFinder_()
  elif choice == 7:
    _Clock_()
  elif choice == 8:
    _HelloLanguage_()
  elif choice == 9:
    _PetSurvay_()
  elif choice == 10:
    _KgToLb_()
  elif choice ==11:
    _Lottery_()
  elif choice==12:
    _ALoneRoom_()
  elif choice==13:
    _lotto_()
  elif choice == 14:
    _calculator_()
  elif choice==15:
    _fruit_()
  elif choice==16:
    _joke_()
  elif choice==17:
    _Username_()
  elif choice ==18:
    _coin_()
  elif choice == 19:
    _area_()
  elif choice == 20:
    _miles_()
  elif choice == 21:
    _timeLived_()
  elif choice == 22:
    _rockpaper_()
  elif choice == 23:
    _card_()
  elif choice == 24:
    _slots_()
  else:
    print("Please select one of the choices.")
    __menu__()

def _loop_():
  _clear_()
  loop=input("Do you want to go back to the menu? y/n")
  loop=loop.lower()
  if loop == "yes" or loop =="y":
    __menu__()
  else:
    print("Goodbye!")

def _NameVarible_():
  _clear_()
  inname=input("Hello! What's your name?")
  print (inname)
  print (inname*1000) 
  print ("Hello " , inname , "!")
  number=6
  print (inname*number)
  print (number)
  _loop_()

def _AnimalChooser_():
  _clear_()
  animals=[ "Monkey",
            "Sloth",
            "Penguin",
            "Snake"]
  colour= input("What is your favourite colour?")
  number= int(input("Choose a number between 1-4"))
  print (animals[number-1])
  print (animals[number-1], " is an amazing animal. You can buy in colour ", colour, " as well.")
  _loop_()

def _Christmas_():
  _clear_()
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
  _loop_()
  

def _Magic8Ball_():
  _clear_()
  responses=["It is certain",
            "Better not tell you now",
            "Out look not so good",
            "Concerntrate and ask again",
            "Yes, certainly",
            "Definely yes",
            "No",
            "Definely no",
            "Ask again another time"]
  askQuestion="y"
  while askQuestion=="y" or askQuestion=="yes":
    question=input ("Ask a Question:")
    print (random.choice(responses))
    askQuestion=input ("Do you want to ask another question:")
    askQuestion=askQuestion.lower()
  _loop_()

def _VatCalculator_():
  _clear_()
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
  _loop_()

def _WinLoseFinder_():
  _clear_()
  #start+varibles
  NumWon=0
  NumLost=0
  NumDrew=0
  postpone=0
  start=input("Welcome to Game counter would you like to input results? y/n")
  start=start.lower()
  #loop
  while start=="yes" or start=="y":
    result=input("How did the game go, did you win, lose or draw?")
    result=result.lower()
    #if won lost or drew
    if result=="win" or result=="won":
      NumWon=NumWon+1
      print("Well done you won!")
    elif result=="lose" or result=="lost":
      NumLost==NumLost+1
      print("Oh well better luck next time!")
    elif result=="draw" or result=="drew":
      NumDrew==NumDrew+1
      print("It is better than losing")
    else:
      postpone=postpone+1
      print("Hope you have another game soon")
  #alble to loop again
    start=input("Would you like to input another result? y/n ")
    start=start.lower()
  #ending program to show all results
  print("You have won an astonding", NumWon, "games!")
  print("Unfortunatly you have lost", NumLost, "games!")
  print("You drew", NumDrew, "games!")
  print("You postponed", postpone, "games!")
  _loop_()


def _Clock_():
  _clear_()
  #varibles
  now = time.localtime()
  hour = now.tm_hour +1
  sec = now.tm_sec 
  minu = now.tm_min 
  days = ["Monday",
         "Tuesday",
          "Wednesday",
          "Thursday",
          "Friday",
          "Saturday",
          "Sunday",
          "Monday"]
  month= now.tm_mon
  months=["December",
          "January",
          "Febuary",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]
  date= now.tm_wday
  day= now.tm_mday
  year=now.tm_year
  #1st 21st 31st
  #2nd 22nd
  #3rd 23rd
  #4th 5th 6th 7th 8th 9th 10th 11th 12th 13th 14th 15th 16th 17th 18th 19th 20th 24th 25th 26th 27th 28th 29th 30th
  # names
  monthName=months[month]
  dayName=days[date]
  if day== 1 or day==21 or day==31:
    print (dayName, day, "st", monthName, year)
  elif day== 2 or day==22:
    print (dayName, day, "nd", monthName, year)
  elif day== 3 or day==23:
    print (dayName, day, "rd", monthName, year )
  else:
    print (dayName, day, "th", monthName, year )
  print(hour, ":",minu,":",sec)
  _loop_()


def _HelloLanguage_():
  _clear_()
  #hello
  print ("hello")
  #start loop
  start ="yes"
  while start !="no":
    lang=input("What language do you want hello in?")
    lang=lang.lower()
  #languages with hello
    if lang=="french":
      print("Bonjour!")
    elif lang=="spanish":
      print("Hola!")
    elif lang=="afrikaans":
      print("Hallo!")
    elif lang=="welsh":
      print("Helo!")
    else:
      print("Sorry not on our system.")
    start=input("Do you want to translate another language? Put no if you do not.")
    start=start.lower()
  print("goodbye")
  _loop_()

def _PetSurvay_():
  _clear_()
  #Welcomeing
  print("Welcome to this pet survey!")
  #varible
  numPets=0
  pets=1
  while pets!=0:
    pets =int(input("How many pets do you have?"))
    numPets=numPets+pets
  print ("Goodbye you have", numPets, "named")
  _loop_()

def _KgToLb_():
  _clear_()
    #Welcome
  print ("Welcome to kg to lb")
  kg = 1
  #loop
  while kg !=0:
    kg=int(input("What do you want to turn into kgs?"))
    lbs=kg*2.2
    print("It is", kg, "kg")
    print("It is", lbs, "lbs")
  #end loop
  print ("goodbye")
  _loop_()

def _Lottery_():
  _clear_()
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
  _loop_()

def _ALoneRoom_():
  _clear_()
  def _intro_():
    Name = input("What is you name?")
    Name = Name.capitalize()
    print("Hello", Name + "! ", "You find your self trapped in a red room. You hear a noise it is just a song. You think it is meowing cat because it is so annoying. You have forgotten everything. Your brain hurts so can only ever process two things.")
    _door_()

  def _door_():
    print ("You look around and all you see is a door. Do you a: learn how to walk or b: walk over to door?")
    walk = input ("A or B?")
    walk = walk.lower()
    door(walk)

  def door(choice):
    if choice == "a":
      print("You chose to learn how to walk. You now know you have some common sense.")
      _buttondoor_()
    elif choice == "b":
      print("You chose to walk. You do not seem very clever.")
      _restwalk_()
    else:
      _error_()

  def _restwalk_():
    print ("You tried to walk to the door but fall down and hit your head. Every thing starts to become more blurry. Do you a: try and keep walking or b:rest until feeling better. ")
    choice = input ("A or B?")
    choice = choice.lower()
    restwalk(choice)

  def restwalk(choice):
    if choice == "a":
      print("You lose your step no one sees you and you are never seen ever again!")
    elif choice == "b":
      print("You chose to rest and find yourself feeling better.")
      _door_()
    else:
      _error_()

  def _buttondoor_():
    print ("It is really strange that their is no one their and then you hear a few footsteps. Do you a: shout for help or b: walk over to the door?")
    walk = input ("A or B?")
    walk = walk.lower()
    buttondoor(walk)
    
  def buttondoor(choice):
    if choice == "a":
      print("You try and shout but you can't. So then you take a deep breath and words flow out your mouth. Suddenly, their is a man who come in dressed in white")
      _fightflight_()
    elif choice == "b":
      print("You find a button next to the door.")
      _button_()
    else:
      _error_()



  def _fightflight_():
    print ("He is coming closer to you. Do you a: fight him or b: run away?")
    walk = input ("A or B?")
    walk = walk.lower()
    fightfligh(walk)
  

  def fightfligh(walk):
    if walk == "a":
      print("You try and knock him out but he is stronger than you. He knocks you out and you wake up not knowing anything.")
      _door_()
    elif walk == "b":
      print("You run out the door for safty.")
      _lr_()
    else:
      _error_()

  def _button_():
    print ("You look closer at the . Do you a: press the button or b: you look at the door?")
    walk = input ("A or B?")
    walk = walk.lower()
    fightfligh(walk)

  def button(walk):
    if choice == "a":
      print("You find a small handle on the door. It opens. Suddenly, their is a man who come in dressed in white.")
      _fightflight_()
    elif choice == "b":
      print("You find a little handle and push it which opens the door. You run out the door to understand everything.")
      _lr_()
    else:
      _error_()

  def _error_():
      print ("sorry error")
      c=input("do you want to start again: y/n")
      c=c.lower()
      if c== "y" or c=="yes":
        _intro_()
      else:
        print ("goodbye")

  def _lr_():
    print ("You look around and theirs two paths Do you a: turn right or b: turn left?")
    walk = input ("A or B?")
    walk = walk.lower()
    lr(walk)

  def lr(walk):
    if choice == "a":
      print("You look and see a police man.")
      _pm_()
    elif choice == "b":
      print("You find a computer.")
      _comp_()
    else:
      _error_()

  def _comp_():
    print ("You walk up to the computer. Do you a: go on the computer on or b: keep walking ?")
    walk = input ("A or B?")
    walk = walk.lower()
    comp(walk)

  def comp(walk):
    if choice == "a":
      print("You were never seen again no one ever knew what happened to you.")
    elif choice == "b":
      print("You get hit by something and you forget everything and find yourself back at the start in an empty room.")
      _door_()
    else:
      _error_()

  def _pm_():
    print ("You walk closer to him and he is on the phone talking about an arest. Do you a: talk to him or b: run away?")
    walk = input ("A or B?")
    walk = walk.lower()
    pm(walk)

  def pm(walk):
    if choice == "a":
      print("You talk to him and he explains that an evil company were trying to turn you into a robot and it was good you escaped as the last test trials died. Later, you found out that you were the next test suject and your spouse at the time had knocked you out and sent you here. You are put in a safe house and live the rest of your life in fear but safe and free.")
      _pm_()
    elif choice == "b":
      print("You run and caught and arrested for the murders of the companies test sujects. You are senteced to life and you plea but it is no use. They do a medical check on you and realise you are not completly human and that the company had put a robot parts to you. You live the rest of your life in prison with evil people looking for you.")
    else:
      _error_()

  _intro_()
  _loop_()


def  _lotto_():
  _clear_()
  print ("Welcome to the National Lottery!")
  start = input("Do you want to start the draw?")

  start=start.lower()
  while True:
    print(random.randrange(1,59))
    start = input("Do you want to draw another number?")
    start=start.lower()

  print("Goodbye")
  _loop_()

def _calculator_():
  _clear_()
  def __main__():
    #welcoming
      print ("Welcome to to the python calculator.")
      start = "yes"
      __start__()
      #start loop to do over and over again
  def __start__():
        # numbers their
        num1 = int(input("What is your first number?"))
        num2 = int(input("What is your second number?"))
        function = input("Do you want to add, subtract, multiply, or divide?")
        function = function.lower()
        if function == "add" or function == "+":
          # +
          __plus__(num1, num2)
        elif function == "subtract" or function == "-":
          # -
          __sub__(num1, num2)
        elif function == "multiply" or function == "x" or function == "*":
          # *
          __X__(num1, num2)
        elif function == "divide" or function == "/" or function == "%":
          #/
          __div__(num1, num2)
        else:
          # go back to start
          start = "yes"

  def __plus__(num1, num2):
    print (num1, "+", num2, "=")
    anser = num1 + num2
    __loop__(anser)

  def __X__(num1, num2):
      print (num1, "x", num2, "=")
      anser = num1 * num2
      __loop__(anser)

  def __sub__(num1, num2):
      print (num1, "-", num2, "=")
      anser = num1 - num2
      __loop__(anser)

  def __div__(num1, num2):
      print (num1, "/", num2, "=")
      anser = num1 / num2
      __loop__(anser)

  def __loop__(anser):
      print (anser)
      start = input ("Do you want another calculation? y/n")
      start = start.lower()
      if start == "yes" or start == "y":
        __start__()
      else:
        print ('Goodbye!')
  __main__()
  _loop_()

def _fruit_():
  _clear_()
  fruit=[ "Apple",
        "Banana",
        "Orange",
       "Pear",
        "Starwberry",
        "Grapes"]
  print (fruit[1])
  _loop_()

def _joke_():
  _clear_()
  def __main__():
  #jokes
    jokes = [
          "Why did the physics teacher break up with the biology teacher?",
          "Why do the French like to eat snails so much?",
          "Husband: Oh the weather is lovely today. Shall we go out for a quick jog?",
          "A guest calls the waiter and complains, 'How come there are no chairs at our table?'!"
          ]
    responses = [
              "There was no chemistry.",
              "They can’t stand fast food.",
              "Wife: Hahaha, I love the way you pronounce Shall we go out and have a cake!",
              "The waiter shrugs, 'I’m sorry but you only booked one table…'"
              ]
    print ("Welcome to the tell-a-joker?")
    joke = "Yes"
    _l_(responses, joke, jokes)

  def _l_(responses, joke, jokes):
    joke = joke.lower()
    if joke == "y" or joke == "yes":
      outjoke = random.randint(1,4)
      print (jokes[outjoke - 1])
      input("")
      print (responses[outjoke - 1])
      __DYWAG_(responses, joke, jokes)
    else:
      print("Goodbye! I hope you enjoyed the jokes.")
      _l_()

 

  def __DYWAG_(responses, joke, jokes):
    joke = input("Do you want another joke? y/n")
    _l_(responses, joke, jokes)

  __main__()
  _loop_()

def _Username_():
  _clear_()
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
    # part of username
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
  _loop_()

def _coin_():
  _clear_()
  import random
  print("Welcome to the coin flip")

  coin = ["Heads",
          "Tails"]
  print (random.choice(coin))
  _loop_()

def _area_():
  _clear_()
  def __main__():
    #welcomes in the program 
    print("Welcome to the area volume maker for cuboid and retangles.")
    _area_()

  def _area_():
    #varibles to keep so we can find areas
    h=float(input("What height is the box in cm?"))
    w=float(input("What width is the box in cm?"))
    l=float(input("What length is the box in cm? If only area put a 0"))
    #asks if 
    if l!=0:
      ans=h * w
      print("Your area is", ans)
      ans=ans *l
      print ("Your volume is", ans)
      __l__()
    else:
      ans=h * w
      print("Your area is", ans)
      __l__()

  def __l__():
    again= input("Do you want to put another area? y/n")
    again = again.lower()
    if again == "y" or again == "yes":
      _area_()
    else:
      print("Goodbye! Thankyou for using this program.")

  __main__()
  _loop_()

def _miles_():
  _clear_()
  speed = int(input("What is your speed"))
  time = int(input("what is your time"))
  ans = speed * time
  print (ans)
  _loop_()

def _timeLived_():
  _clear_()
  def __main__():
    print ("Welcome to the date today born finder!")
    _dob_()

  def _dob_():
    # finding out the date of birth of the person
    dobd = int(input ("What is your day you were born?"))
    dobm = int(input ("What is your mounth you were born number?"))
    doby = int(input ("What is your year you were born?"))
    # date born
    born = datetime.date(doby, dobm, dobd)
    _date_(born, )
    _loop_()


  def _date_(born):
    now = time.localtime()
    # finding the date today
    day = now.tm_mday
    year = now.tm_year
    month= now.tm_mon
    # making date of today
    today = datetime.date(year, month, day)
    #verifying the born
    born = born
    #moving born and today across the functions
    _days_(born, today)
    


  def _days_(born, today):
    #making the idea of how many days lived for. date today takeaway born date
    days = today - born
    print (days)
    # verifying the varible
    _seconds_(born, today)

  def _seconds_(born, today):
    #making it in _seconds_
    borns = time.mktime(born.timetuple())
    todays = time.mktime(today.timetuple())
    second = todays - borns
    print(second, "seconds")

  __main__()
  _loop_()

def _rockpaper_():
  _clear_()
  def _main_():
    # getting varible choices
    rps = [
            "rock",
            "paper",
            "scissors"
            ]
    # VARIBLES TO USE IN THE Future
    win = 0
    lose = 0
    draw = 0
    #welcome
    print ("Welcome to rock paper scissors")
    _choices_(rps, win, lose, draw)

  def _choices_(rps, win, lose, draw):
    #users idea choice chosen and under that computer chosen
    choice= input("Rock, paper or scissors:")
    choice= choice.lower()
    if choice != "rock" and choice != "paper" and choice != "scissors":
      _choices_(rps, win, lose, draw)
    else:
      computer = random.choice(rps)
      print ("You chose", choice,)
      print ("The computer chose", computer)
      _if_(choice, win, lose, draw, computer, rps)

  def _if_(choice, win, lose, draw, computer, rps):
    if choice == "rock" and computer == "scissors":
      win = win +1
      _loop_(win, lose, draw, rps)
    elif choice =="scissors" and computer == "rock":
      lose = lose + 1
      _loop_(win, lose, draw, rps)
    
    elif choice =="paper" and computer == "rock":
      lose = win + 1
      _loop_(win, lose, draw, rps)

    elif choice =="rock" and computer == "paper":
      lose = lose + 1
      _loop_(win, lose, draw, rps)

    elif choice =="scissors" and computer == "paper":
      lose = win + 1
      _loop_(win, lose, draw, rps)

    elif computer =="scissors" and choice == "paper":
      lose = lose + 1
      _loop_(win, lose, draw, rps)

    else:
      draw = draw +1
      _loop_(win, lose, draw, rps)

  def _loop_(win, lose, draw, rps):
    print("Won:", win)
    print("lost:", lose)
    print("draw:", draw)
    loop = input("Do you want another game? y/n")
    loop = loop.lower()
    if loop == "y" or loop == "yes":
      _choices_(rps, win, lose, draw)
    else:
      print ("You won", win, "games.")
      print ("You lost", lose, "games.")
      print ("You drew", draw, "games.")
      print ("Goodbye")

  _main_()
  _loop_()

def _card_():
  _clear_()
  #importing of information needed
  import csv
  import random
  import time
  def _login_():
    #defined varibles
    uscore1 = 0
    uscore2 = 0
    count = 0
    found1 = False 
    found2 = False
    #letting a loop to makesure that one user atleast is incorrect
    while found1 == False or found2 == False:
      #input users
      User1 = input ("Username for player 1:")
      Pass1 = input ("Password for player 1:")
      found1 = False
      #opening files password.txt and username.txt
      username = open("username.txt","r")
      password = open("password.txt","r")
      #reading the files
      usernamelines = username.readlines()
      passwordlines = password.readlines()
      #searches to see if password is equal to password
      for i in range(len(usernamelines)):
        if User1 == (usernamelines[i].strip('\n')) and Pass1 == (passwordlines[i].strip('\n')):
          found1 = True
      #inputs user and password 
      User2 = input ("Username for player 2:")
      Pass2 = input ("Password for player 2:")
      found2 = False
      #opens file
      username = open("username.txt","r")
      password = open("password.txt","r")
      #reads file
      usernamelines = username.readlines()
      passwordlines = password.readlines()
      #searches to check username and passwords are right
      for i in range(len(usernamelines)):
        if User2 == (usernamelines[i].strip('\n')) and Pass2 == (passwordlines[i].strip('\n')):
          found2 = True
        #validation to check passwords
      if User1 == User2:
        print("Sorry used the same usernames for both")
        found1 = False
        found2 = False
      elif found1 == True and found2 == True:
            _rounds_( User1, User2, Pass1, Pass2, uscore1, uscore2)
      elif found2 == True:
        print ("Sorry login details not accepted for player 1. Please try again.")
      elif found1 == True:
        print ("Sorry login details not accepted for player 2. Please try again.")
      else:
        print ("Sorry login details not accepted for both username. Please try again.")
      count = count + 1
      if count ==4:
        print ("Sorry unable to keep going as unfound credentials 4 times.")
        exit()
    
      
  def _player1_(Uscore1):
    #player1 scoreing 
    print ("Player 1:")
    score = __roll__()
    Uscore1 = Uscore1 + score
    #check above 0
    if Uscore1 <= 0:
        Uscore1 = 0
    return Uscore1

  def _player2_(Uscore2):
    # player 2 scoring
    print ("Player 2:")
    score = __roll__()
    Uscore2 = Uscore2 + score
    #check above 0
    if Uscore2 <= 0:
      Uscore2 = 0
    return Uscore2

  def __roll__():
    #varbles set
    score = 0
    playerextra = 0
    player = [1,2,3,4]

    #rolls twice
    for i in range (0,2,1):
      input("And your roll is:")
      player[i]= random.randrange(1,6)
      print("You rolled a", player[i], "!")

  #allows extra roll if doubles
    if player[0] == player[1]:
      print("You rolled a double so an extra roll")
      input("And your roll is:")
      playerextra= random.randrange(1,6)
      print("You rolled a", playerextra, "!")
    
    player1 = player[0] + player[1] + playerextra
    e = [2,4,6,8,10,12]
    #score is added
    if player1 in e:
      score = score + 10 + player1
    else:
      score = score - 5
    print ("Your score this round is", score, "!")
    #scor is returned to player
    return score
  
  def _clear_():
    #waits 1.5 seconds
    time.sleep(1.5)
    import os
    #clears screen
    os.system('clear')
    return

  def _rounds_(User1, User2, Pass1, Pass2, uscore1, uscore2):
    #declared varibles
    Uscore1 = 0
    Uscore2 = 0
    # allows 5 rounds
    for i in range (1,6, 1):
      _clear_()
      print ("Round", i, ":")
      Uscore1 = _player1_(Uscore1)
      print ("Player 1 score after the round is ", Uscore1)
      Uscore2=_player2_(Uscore2)
      print ("Player 1 score after the round is ", Uscore2)
    #sees if scores are the same
    while Uscore1 == Uscore2:
      _clear_()
      #lets both to roll
      print("Player 1 score:", Uscore1)
      print("Player 2 score:", Uscore2)
      print("Sudden death:")
      Uscore1=_player1_(Uscore1)
      Uscore2=_player2_(Uscore2)
      print("Player 1 score:", Uscore1)
      print("Player 2 score:", Uscore2)
      #checking who wins
    if Uscore1 > Uscore2:
      print("Player 1 wins!")
      highscore= Uscore1
      user = User1
    elif Uscore1 < Uscore2:
      print("Player 2 wins!")
      highscore= Uscore2
      user = User2
    else:
      print("ERROR!")
      _rounds_(User1, User2, Pass1, Pass2, uscore1, uscore2)
    _HS_(user, highscore)

  def _HS_(user, highscore):
    #opens file saves new score
    with open ('score.csv', 'a', newline='') as CSVSCORES:
      write = csv.writer(CSVSCORES, delimiter=',')
      write.writerow([user,highscore])
    CSVSCORES.close()
    _sort_()

  def _sort_():
    #opens file
    score2=[]
    csv_HS = open('score.csv', 'r')
    HSData = csv.reader(csv_HS, delimiter=',')
    scores = []
    #varible list set for scores and score2
    for row in HSData:
      scoretoadd = row[1] + " - " + row [0]
      score=row[1]
      score2.append(scoretoadd)
      scores.append(score)
    for row in HSData:
      scoretoadd = row[1] + " - " + row [0]
      score2.append(scoretoadd)
    #bubble sort
    n = len(scores)
    swapped = True
    while n > 0 and swapped == True:
      swapped = False
      n = n - 1
      for i in range(0,n,1):
        p = i+ 1
        if int(scores[i]) < int(scores[i+1]):
          temp = scores[i]
          scores[i] = scores[n]
          scores[n] = temp
          swapped = True 
    high=score2
    #searches person who worked
    for n in range (0,len(scores),1):
      for i in range (0, len(score2),1):
        x = str(scores[n]) in str(score2[i])
        if x == True:
          high[n]= score2[i]
          break
    #lists highscores
    print("The 5 biggest numbers are:")
    if len(scores) <5:
      for i in range (0,len(high),1):
        print(high[i])
    else:    
      for i in range (0,5,1):
        print(high[i])
      

  _login_()
  _loop_()


def _slots_():
  _clear_()
  import random
  def _main_():
      #diffrent opptions in game
      slots = ["coin",
                "7",
                "dimond",
                "cherry",
                "bar",
                "bell",
                "oranges"]
      #random.choice
      # this choses the slot and says it
      slotOne = random.choice(slots)
      print (slotOne)
      slotTwo = random.choice(slots)
      print (slotTwo)
      slotThree = random.choice(slots)
      print (slotThree)
      
      find(slotOne, slotTwo, slotThree,)

  def find( slotOne, slotTwo, slotThree):
      if slotOne == slotTwo == slotThree:
          print ("You win")
      else:
          print ("Unfortuneatly, you lose!")

  _main_()
  _loop_()


__main__()