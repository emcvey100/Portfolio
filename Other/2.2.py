def temp():
  choice=input("""What do you want to find out?
    1) celsius to fahrenheit
    2) fahrenheit to celsius
    Please enter 1/2:""")
  if int(choice) ==1:
    celsius()
  elif int(choice) ==2:
    fahrenheit()
  else:
    temp()

def celsius():
  value=int(input("What value do you want to convert?"))
  value= value * 9/5 
  value=round(value,2)+32
  print(value)

def fahrenheit():
  value=int(input("What value do you want to convert?"))
  value= value-32
  value=round(value*5/9,2)
  print(value)

def money():
  choice=input("""What do you want to find out?
    1) £ to $
    2) $ to £
    Please enter 1/2:""")
  if int(choice) ==1:
    pound()
  elif int(choice) ==2:
    dollar()
  else:
    money()
def pound():
  value=int(input("What value do you want to convert?"))
  value=round(value*1.25,2)
  print (value)

def dollar():
  value=int(input("What value do you want to convert?"))
  value=round(value/1.25,2)
  print (value)
def volume():
  choice=input("""What do you want to find out?
    1) cubic metres to imperial pint 
    2) imperial pint to cubic metres
    Please enter 1/2:""")
  if int(choice) ==1:
    metre()
  elif int(choice) ==2:
    pint()
  else:
    volume()
def pint():
  value=int(input("What value do you want to convert?"))
  value=round(value/1759.75,2)
  print (value)
def metre():
  value=int(input("What value do you want to convert?"))
  value=round(value*1759.75,2)
  print (value)
def main():
  choose=int(input("""What type of conversion?
    1)temprature
    2)currency
    3)volume
    Please enter 1/2/3:"""))
  if choose==1:
    temp()
  elif choose==2:
    money()
  elif choose==3:
    volume()
  else:
    main()
main()