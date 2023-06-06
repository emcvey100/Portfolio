list1=[1,2,3,4,5,6]

def rotate(list1):
  length=len(list1)/3
  new=[]
  for i in range(round(length),round(length*3)):
    new.append(list1[i])
  for i in range(0,round(length)):
    new.append(list1[i])
  return new
    
    

newList=rotate(list1)
print(newList)