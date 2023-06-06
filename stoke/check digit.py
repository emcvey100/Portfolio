def _barcode_(bar_code):
  checkdigit=bar_code[len(bar_code)-1]
  #print(checkdigit)
  numbers=bar_code[0:len(bar_code)-1]
  #print(numbers)
  result=0
  for i in range(len(numbers)):
    if numbers[i].isdigit()==False:
      return False
    else:
      position=int(bar_code[i])
    weight=10-i
    current=weight*position
    result+=current
  mod11=result%11
  if mod11==10:
    if checkdigit=="X":
      return True
    else:
      return False
  elif mod11==0:
    if checkdigit=="0":
      return True
    else:
      return False
  mod11=11-mod11
  #print(mod11)
  if checkdigit==str(mod11):
    return True
  else:
    return False

code=input("Barcode:")
if _barcode_(code)==True:
  print("Valid barcode!")
else:
  print("Invalid barcode!")
  #1858134153