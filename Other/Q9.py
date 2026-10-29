def __main__():
  NewNum=""
  number= input("Please give a number:")
  i=0
  while i < len(number):
    NewNum=number[i]+NewNum
    i=i+1
  print(NewNum)
  if NewNum==number:
    print(True)
    return True

__main__()