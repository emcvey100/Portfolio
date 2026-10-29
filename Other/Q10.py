list1=[1,2,46,4654,6587,54,76,76,54,57,45,78,34,9,5,2,1,0]
list2=[2,46,6,79,1,3,6,8,3,6,576,76,43,78]
n=0
newlist=[]
for i in list1:
  if i%2 == 1:
    newlist.insert(n,i)
    n=n+1
for i in list2:
  if i%2 == 0:
    newlist.insert(n,i)
    n=n+1
print(newlist)