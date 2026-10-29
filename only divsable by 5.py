#Given a list of numbers, wite a program that iterates the list and prints only those numbers which are divisable by 5
nums=[]
for i in nums:
    calc = i%5
    if calc ==0 and i !=0:
      print(i)
