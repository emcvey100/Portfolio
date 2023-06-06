n=int(input("Please eneter a number?:"))
num=0
nums=""
for i in range(1, n, 1):
  if (num+i)<=n:
    num=num+i
    if nums=="":
      nums=str(i)
    else:
      nums=nums + "+" + str(i)
print(nums)