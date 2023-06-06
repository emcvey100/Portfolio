#input 4 digits
pin=input("Enter digits:")
def check(p):
  #check only  length of 4
  if len(pin)!=4:
    return False
  #check all numbers
  elif pin.isdigit() != True:
    return False
  else:
    return True

while check(pin)==False:
  #while check is not true input new 4 digits#
  pin=input("Please enter correct 4 digits:")

#swap positions
#change starter
#print variation
for first in range (4):
  for second in range(4):
    if first != second:
      for third in range(4):
        if first != third and second != third:
          for fourth in range (4):
            if first != fourth and second != fourth and third != fourth:
              print(pin[first], pin[second], pin [third], pin[fourth])
