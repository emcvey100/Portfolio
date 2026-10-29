#bubble sort sorts the list into numerical or reverse alphabetical order
#list to sort in order
Listn = [1,23,3,52,9,9,25,6,7,28,53,2,6]
# varibe of the number of leght in list 
num=len(Listn) 
# swap at is true right now
swap = True 
#while length of list is bigger than zero and 
while num > 0 and swap == True:
  # swap is not true
  swap = False
  # number is one less
  num = num -1
  # do this code from 0 to number
  for i in range (0, num):
    #if list number bigger than next number
    if Listn[i] > Listn[i+1]:
      # move list number into temp
      temp = Listn [i]
      # list number equals next list number
      Listn [i] = Listn [i + 1]
      # the next list number now equals number
      Listn [i+1]=temp
      swap = True

  # swap is now true
  
# prints the ordered list
print (Listn)
