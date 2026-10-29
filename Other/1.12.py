def LetterChanges(string):
  word=[]
  for i in string:
    letter=i
    num=ord(letter)
    word.append(num)
  for i in range (0, len(word)):
    word[i]=int(word[i])+1
    if word[i]==123:
      word[i]=97
    word[i]=chr(word[i])
  new=""
  for i in range (0, len(word)):
    if word[i]=="i" or word[i]=="e" or word[i]=="a" or word[i]=="o" or word[i]=="u":
      word[i]=word[i].capitalize()
    new=new+word[i]
  return new


string=input("Word:").lower()

print(LetterChanges(string))