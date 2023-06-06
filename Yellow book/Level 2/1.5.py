import datetime
year=datetime.datetime.now()
year=year.year
leap_year=0
while leap_year != 200:
  if (year%4) ==0 or (year%400)==0:
    print(year)
    leap_year=leap_year+1
  year=year+1
