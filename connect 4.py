def start():
  #names called
  names = names()
  #random choice who starts
  import random
  first=random.randint(1,2)
  print(names[first], " gets to start.")
  #choose red or yellow
  fc=input("What colour do you want t")
  #make names 2d and append red and yellow to lists  
  #first player fist in list
  #return name list
  
def names():
  name=lambda n: input("Please enter your name:").capitalize()

  clear()
  persons=[name(1),name(2)]
  import random
  num=random.randint(0,1)
  clear()
  print(persons[num], " gets to start!")
  if num==1:
    n2=0
  else:
    n2=1
  col=color()
  return [[persons[num],col[0]],[persons[n2],col[1]]

def game():
  pass
  #clear board
#i=i+1
#if i ==3 then i=1
#show board
#let player  go
#run valid to see if can fit or won 
#if unvalid play part again
#if 2 players gone and not won do  game again
  
def valid():
  #is colum full
  # / check
  #- check
  #|check
  #\ check

  pass
def clear():
  #import os and clear
  pass
def end():
  #say if draw or who won
  #ask if want a loop
  #if want loop go back to game
  #if no loop then  goodbye
  pass
#welcoming the game and what it is about
print("""     Connect 4
Join 4 counters in a row before the other to win.""")
start()