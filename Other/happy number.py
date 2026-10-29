def happy_number(num):
  if int(num) == 4:
      print("No Happy Number")
  elif int(num) == 1:
      print("Happy Number")
  else:
    do(num)

def do(num):
    new=0
    for i in str(num):
      new+=square(i)
    happy_number(new)

def check(n):
  if n.isnumeric()==True:
    return int(n)
  else:
    check(input("Enter a real number:"))

square=lambda numbers : int(numbers)**2
number=check(input("Enter a number:"))
happy_number(number)