#binary search has to be in order so it finds the middle of the list and sees if it is higher or lower and then looks at that section then repeats until it is found
#this is more effective than a linear search
#list in order of number that want to search through
item_list = [1,2,3,4,5,6,7,8,9]
#varible called item asking person what number they want to find
item = int (input("Number:"))
#the inital starting point is 0
first = 0
#the inital ending point is the last number in list
last = len(item_list)-1
#the number has not been found so varible is false
found = False
# until end ponit is bigger than start point carry and it has not been found  on doing the more indented code
while( first<=last and not found):
	 #the mid point is the start point add the end point divided by 2
  mid = (first + last)//2
	#if the midpoint number in list is equal to item
  if item_list[mid] == item :
    #found is now true as found so itteration stops.
    found = True
    #if the midpoint number in list is not equal to item
  else:
# if the mid point is less than target make the last one lessthan midpoint(two lines) 
    if item < item_list[mid]:
      last = mid - 1
    # if target is bigger than midpoint do make the first the same as the midpoint but add one.(two lines)
    else:
      first = mid + 1	
# if the number is in the list print number has been found
if found:
  print("number has been found")
# if the number is not in the list print the number not been found
else:
  print("Number not found")