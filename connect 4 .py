def g(profile,board,bp):
  for player in range(2):
    clear()
    board(board)
    print("Its your turn "+profile[player][1]+"!")
    c=input("Please input a colomn where you want your piece to go:").upper()
    board=update(profile[player][2], c,board,bp)
    return board

def board(boards):
  print("The board currently looks like:")
  for i in range(6):
    line=""
    for b in boards:
      line += str(boards[b][i])+" "
    print(line)
  line=""
  for o in boards:
    line+=o+" "
  print(line)

def update(color,column, b, boardpointer):
  pass

def color():
  color=input("Would you like to be Red(r) or Yellow(y)?").lower()
  if color=="yellow" or color=="y":
    return "Y","R"
  elif color=="red" or color=="r":
    return "R","Y"
  else:
    color()

def loop():
  pass

def clear():
  import os
  os.system('cls')
  os.system('clear')

print("""     Connect 4
Join 4 counters in a row before the other to win.""")

def player():
  clear()
  persons=[input("Please enter your name:").upper(),input("Please enter your name:").upper()]
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
def start():
  n=player()
  b={"A":[0,0,0,0,0,0],"B":[0,0,0,0,0,0],"C":[0,0,0,0,0,0],"D":[0,0,0,0,0,0],"E":[0,0,0,0,0,0],"F":[0,0,0,0,0,0],"G":[0,0,0,0,0,0]}
  boardpointer={"A":0, "B":0,"C":0,"D":0, "E":0,"F":0,"G":0}
  board(b)
  g(n,b,boardpointer)
  clear()
  loop()
start()
