n=int(input("Enter a number:"))
num=0
for i in range(1,n+1):
  if i%3 == 0 or i%5 ==0:
    num = num+i
print(num)