list1=[1,2,3,4,5]
list2=[10,11,12,13,14]

def concatenates(list1,list2):
  new=[]
  for i in list1:
    new.append(i)
  for i in list2:
    new.append(i)
  return new
newList=concatenates(list1,list2)
#print(newList)