# linear search list one by one to see if that is the number that you want
def __main__():
  # listing the varible with all the numbers allready in database
  List =  [74, 32, 16, 34, 9, 17, 44]
  found = False
  # askes the user what number to search
  numSearched= int(input("Number:"))
  #iteration loop for the number in the List
  for i in range(0, len(List)):
  # if number searched is equal to the list number do this code 
   if List[i]==numSearched:
     # tell that number found
     print ("Number found in ", List )
     # The number has been found
     found = True
     # stop the iteration
     break
# if number not found in whole list this code has been done
  if found ==False:
    # print that number is not found
    print("Number not found in", List)
  
__main__()