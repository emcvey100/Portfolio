import random
def _maketicket_():
  ticket=[[0,   0,   0,   0,   0,   0,   0,   0,   0], [0,   0,   0,   0,   0,   0,   0,   0,   0], [0,   0,   0,   0,   0,   0,   0,   0,   0]]

  for row in range (3):
    high=(row+1)*10
    low=high-9
    for col in range(9):
      found=False
      while found==False:
        found=True
        x=random.randint(low,high)
        for i in range(col):
          if x == ticket[row][i]:
            x=random.randint(low,high)
            found=False
        ticket[row][col]=x
    num=[0,0,0,0]
    for n in range(4):
      num[n]=random.randint(0,8)
      for i in range(n):
        if num[n] == num[i]:
          num[n]=random.randint(0,8)
      ticket[row][num[n]]=0
  return ticket

def _printticket_(prticket):
  for row in range(3):
    line=""
    for col in range(9):
      line+="|"
      if prticket[row][col]==0:
        line+="__"
      else:
        found=False
        for i in range(10):
          if prticket[row][col]==i:
            found=True
            line+= "0"+str(i)
        if found ==False:
          line+=str(prticket[row][col])
    print(line)

input()
_printticket_(_maketicket_())