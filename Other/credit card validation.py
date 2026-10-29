
def check(pin):
  allsum=int(pin[len(pin)-1])
  numdigit= len(pin)
  mod=numdigit%2
  for i in range(numdigit-2):
    dig=int(pin)
    if i % 2==mod:
      dig= dig*2
    if dig>9:
      dig-=9
    allsum+=dig
  if allsum%10 ==0:
    return("Accepted")
  else:
    return("Rejected")
print(check(input("Number:")))

