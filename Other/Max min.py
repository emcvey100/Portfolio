Numbers=[]
maximun=[0,0]
minimun=[0,0]
av=[0,0,0]
total=0
for i in range(20):
  Numbers.append(int(input("Please enter a number between 1-100:")))
  while Numbers[i]<0 and Number[i]>100:
    Number[i]=int(input("Please enter a number between 1-100:")))
  
  if Numbers[i]>maximun[0]:
      maximun[0]=Numbers[i]
      maximun[1]=i
  elif Numbers[i]<minimun[0]:
      minimun[0]=Numbers[i]
      minimun[1]=i
for i in Numbers:
  total+=i
av[0]=total/20
for i in Numbers:
  if av[1]<i<av[0]:
    av[2]=i
    av[1]=i
print("The maximum is "+maximun[0]+" located "+maximun[1])
print("The minimum is "+minimun[0]+" located "+minimun[1])
print("The average is "+av[0]+" which is closet to "+av[1]+" located "+av[2])