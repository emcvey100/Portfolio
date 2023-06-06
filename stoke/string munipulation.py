def change(letter):
  let=ord(letter)
  if let<=72:
    let+=13
  else:
    let-=13
  return chr(let)

startText=input("Please input what you want to encode").upper()
newText=""
for i in startText:
  if ord(i) <=65 and ord(i) >=91:
    newText+=change(i)
  else:
    newText+=i
print(newText)