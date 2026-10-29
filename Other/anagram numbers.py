def types(number):
  numlist=[0,0,0,0,0,0,0,0,0,0]
  #putting into single number types
  for num in range(10):
    for i in str(number):
      #print(i)
      #print(num)
      if num==i:
        numlist[num]+=1
      #print (numlist[num])
  return numlist

mult=lambda a, n: a*n

def loop(num, first):
  print(1)
  for i in range(9):
    if types(mult(i,num))==first:
      print(types(mult(i,num)))
      print(first)
      return True
  return False

intnum=int(input("Number:"))
print(loop(intnum,intnum))
if loop(intnum,intnum)==True:
  print("Is an anagram number")
else:
  print("Not an anagram")

#1246878











