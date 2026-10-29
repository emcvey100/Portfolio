letter="A"
def encrypt(letter):
  letter= ord(letter.upper())
  if letter <=78:
    letter-=13
  else:
    letter+=13
  return char(letter)
print(encrypt(letter))