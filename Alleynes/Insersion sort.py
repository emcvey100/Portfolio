# insertion sort looks at the first number in the list and says it is in the right place then it looks at the second and see where to put it by looking down the list so far and carries on like that till all list is done.
def __main__():
  #list of numbers needing to be sorted
  c=0
  s=0
  n=320
  Listnum=[]
  while n > 1:
        Listnum.append(n)
        n -= 1
  #do number i by 1 by lenth of Listnum
  for i in range (1,len(Listnum),1):
    # varible to say the number that the computer is looking at
    current= Listnum [i]
    # varible saying the number i is
    extra = i
    #irreration loop of extra being more than 0 and the next list number is more than current number
    while extra > 0 and Listnum[extra-1] > current:
      c=c+1
      # the number to place is then move across and looked to see if now is in position
      Listnum [extra] = Listnum[extra-1]
      extra = extra -1
      s=s+1
    # the list number when in the right place is slotted in the right place
    Listnum[extra]=current
    # prints user the right code
  print(c)
  print(s)
  print (Listnum)

__main__()