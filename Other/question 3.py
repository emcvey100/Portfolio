def _letter_(letter):
  lets={"A":"B","B":"AB","C":"CD","D":"DC","E":"EE"}
  return lets[letter]


def word(word):
  new=""
  for i in word:
    new+=_letter_(i)
  return new
correct=False
while correct==False:
  correct=True
  string=input("Input the three letters:")
  for i in string:
    if i!="A" and i!="B" and i!="C" and i!="D" and i!="=E":
       if correct==False or len(string)!=3:
         correct=False 

intergers=input("Please input two intergers the first for amount of steps the second for the position to.").split()
for i in range(2):
  intergers[i]=int(intergers[i])
for i in range(intergers[0]):
  string=word(string)
numbers={"A":0,"B":0,"C":0,"D":0,"E":0}
n=0
for i in string:
  if n<intergers[1]:
    numbers[i]+=1
  n+=1
line=""
for i in numbers:
  line+=str(numbers[i])
print(line)

