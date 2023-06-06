list1=[1,2,3,4,6,8,9]
def odd(list1):
  new=[]
  for i in range(1,(len(list1)),2):
    new.append(list1[i])
    #print(i)
  return new
New=odd(list1)
#print(New)