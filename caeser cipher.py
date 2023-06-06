inputword=input(":").lower()
def caeser(word):
  new=""
  for i in word:
    asc=ord(i)
    asc=+1
    if asc>122:
      asc=asc-26
    print(chr(asc))
    print(asc)
    new += chr(asc)
  return new

print(caeser(inputword))