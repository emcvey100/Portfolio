list1=[1,2,3,4,6,8,9]
def computes(list1):
  new=0
  for i in list1:
    new=new+i
  return new
New=computes(list1)
print(New)