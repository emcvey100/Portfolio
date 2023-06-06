spl=False
nums="£%"
while nums[0].isalpha()==True and nums[1].isalpha()==True or spl==False:
  nums=input("Enter 2 numbers X, Y:")
  spl=False
  for i in range(len(nums)-2):
    x= nums[i]+nums[i+1]
    if x==", ":
      spl=True
  if spl==True:
    nums=nums.split(", ")
array=[]
for i in range(int(nums[0])):
  x=[]
  for n in range(int(nums[1])):
    new=n*i
    x.append(new)
  array.append(x)
for i in range(int(nums[0])):
  for x in range(int(nums[1])):
    n=str(array[i][x])
    if x==0:
        line=n
    else:
        line+=" ," + n
  print(line)
