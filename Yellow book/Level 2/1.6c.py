list1=[1,2,3,4,5]
list2=[10,11,12,13,14]

def combine(list1,list2):
  new=[]
  if len(list1)<len(list2):
    length=len(list2)
  else:
    length=len(list1)
  for i in range(0,length):
    new.append(list1[i])
    new.append(list2[i])
  return new
newList=combine(list1,list2)
print(newList)