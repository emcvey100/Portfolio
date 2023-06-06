n=int(input("Enter a number:"))
product=input("Do you want to give the product or the sum?:").capitalize()
if product=="Product":
  num=1
  for i in range(1,n+1):
    num = num*i
else:
  num=0
  for i in range(1,n+1):
      num = num+i
print(num)