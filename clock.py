# import
import time
#varibles
now = time.localtime()
hour = now.tm_hour +1
sec = now.tm_sec 
minu = now.tm_min 
days = ["Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
        "Monday"]
month= now.tm_mon
months=["December",
        "January",
        "Febuary",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]
date= now.tm_wday
day= now.tm_mday
year=now.tm_year
#1st 21st 31st
#2nd 22nd
#3rd 23rd
#4th 5th 6th 7th 8th 9th 10th 11th 12th 13th 14th 15th 16th 17th 18th 19th 20th 24th 25th 26th 27th 28th 29th 30th
# names
monthName=months[month]
dayName=days[date]
if day== 1 or day==21 or day==31:
  print (dayName, day, "st", monthName, year)
elif day== 2 or day==22:
  print (dayName, day, "nd", monthName, year)
elif day== 3 or day==23:
  print (dayName, day, "rd", monthName, year )
else:
  print (dayName, day, "th", monthName, year )
print(hour, ":",minu,":",sec)
#print(now)