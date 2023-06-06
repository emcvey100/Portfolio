string="racecar"
def palindrome(string):
  new=""
  for i in string:
    new=i+new
  if string==new:
    return True
  return False
New=palindrome(string)
print(New)