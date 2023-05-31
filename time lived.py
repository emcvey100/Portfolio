#importing the time and datetime
import datetime
import time

def __main__():
  print ("Welcome to the date today born finder!")
  _dob_()

def _dob_():
  # finding out the date of birth of the person
  dobd = int(input ("What is your day you were born?"))
  dobm = int(input ("What is your mounth you were born number?"))
  doby = int(input ("What is your year you were born?"))
  # date born
  born = datetime.date(doby, dobm, dobd)
  _date_(born, )

def _date_(born):
  now = time.localtime()
  # finding the date today
  day = now.tm_mday
  year = now.tm_year
  month= now.tm_mon
  # making date of today
  today = datetime.date(year, month, day)
  #verifying the born
  born = born
  #moving born and today across the functions
  _days_(born, today)

def _days_(born, today):
  #making the idea of how many days lived for. date today takeaway born date
  days = today - born
  print (days)
  # verifying the varible
  _seconds_(born, today)

def _seconds_(born, today):
  #making it in _seconds_
  borns = time.mktime(born.timetuple())
  todays = time.mktime(today.timetuple())
  second = todays - borns
  print(second, "seconds")


__main__()

