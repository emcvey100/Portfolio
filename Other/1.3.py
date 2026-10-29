
for n in range(2,100,1):
  prime=True
  for i in range(2,n):
    if n%i==0:
      prime=False
  if prime==True:
    print(n)