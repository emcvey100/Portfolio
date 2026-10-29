#Write a maths quiz with three questions.
#It must ask the user to input their name at the start.
#At the end t should display a message informing the user of their score.
#Write a function that saves the user's name and quiz result in a text file.
#Extend your maths quiz program from Challenge 20 by including a list of the scores that have been taken the quiz before.
#Improve your maths quiz form challenge 10 and 27 by storing all the questions and possible anwsers in a two-dimentional array.
#write a function that can reuse to ask each question
def __main__():
  print ("""Welcome to the maths quiz.""")
  print ("scores")
  file = open("scores.txt", "r")
  for line in file:
      print(line)
  Score=0
  name=input("""What is you name""")
  name = name.capitalize()
  score=_Questions_(score)
  StudentScore(name,score)

def StudentScore(name, score):
  file = open("scores.txt", "a")
  file.write("\nName: "+name+" Score: "+str(score))
  file.close()
import random
def _Questions_(score):
  database = [["2+3","2*0","10*10","100-1","5*2","11+11"][5,0,100,99,10,22]]
  num=random.randint(len(database))
  question = int(input(database[0][num]))
  if question == ans[1][num]:
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
__main__()
