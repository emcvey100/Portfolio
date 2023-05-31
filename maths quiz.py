def __main__():
  print ("""Welcome to the maths quiz.""")
  _time_()
  Score=0
  name=input("""What is you name""")
  name = name.capitalize()
  _Question1_(score)
  _Question2_(score)
  _Question3_(score)
  _Question4_(score)
  _Question5_(score)
  StudentScore(name )

def _time_():
  import time
  now = time.localtime()
  month= now.tm_mon
  day= now.tm_mday
  year=now.tm_year
  print( """Today's Date:
  """day, "/", month, "/", year)
  return

def _Question1_(score):
  print("""Question 1:
  What is 22+76?""")
  Question = int(input(""))
  ans = 98
  if Question == ans1:
    _correct_(score)
  else:
    _wrong_(ans)
    return

def _correct_(score):
  print ("""Well Done that was corrrect.""")
  score = 0 + 1
  return

def _wrong_(ans):
  print ("""Unfortunatly that was incorrect.
  the answer is""", ans)
  return

def _Question2_(score):
  print("""Question 2:
  What is 2+7?""")
  Question = int(input(""))
  ans = 9
  if Question == ans1:
    _correct_(score)
  else:
    _wrong_(ans)
    return

def _Question3_(score):
  print("""Question 3:
  What is 88+2?""")
  Question = int(input(""))
  ans = 90
  if Question == ans1:
    _correct_(score)
  else:
    _wrong_(ans)
    return

def _Question4_(score):
  print("""Question 4:
  What is 2X2?""")
  Question = int(input(""))
  ans = 4
  if Question == ans1:
    _correct_(score)
  else:
    _wrong_(ans)
    return

def _Question5_(score):
  print("""Question 1:
  What is 7X7?""")
  Question = int(input(""))
  ans = 49
  if Question == ans1:
    _correct_(score)
  else:
    _wrong_(ans)
    return
__main__()