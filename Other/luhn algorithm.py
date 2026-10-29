def luhn(number):
  new=0
  mod=0
  for i in range(len(number)):
    if number[i].isdigit()==False:
      return False
    if i %2==1:
      value=int(number[i])*2
      if value>9:
        val=0
        for i in str(value):
          val+=i
        value=val
    else:
      value=int(number[i])
    new+=str(value)
    mod+=value
  if mod%10==0:
    return True
  else:
    return False

pin=input("Pin:")
if luhn(pin)==True:
  print("Valid")
else:
  print("Invalid")