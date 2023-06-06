num=[6,7,1,3,2,1]
def compute(num):
  new=0
  length=0
  while len(num)!=length:
    new=new+num[length]
    length=length+1
  return new
x=compute(num)
print(x)