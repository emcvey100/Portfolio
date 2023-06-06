from datetime import datetime

def isWeekday(mydate):
    day = mydate.weekday()  #Get the nunber of the day of the week - Monday = 0, Tuesday = 1 etc.
    if day < 5:
        return True
    else:
        return False

# Calls the function providing a date
workday = isWeekday(datetime.now())  #Call the isWeekday function with today's date, store the returned data in a variable "workday".

if isWeekday(datetime.now()):
    print("It is a week day")
