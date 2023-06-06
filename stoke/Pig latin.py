word = input("Enter a word:")
start=""
end=""
x=False
for i in word:
  if i== "a" or i =="e" or i=="o" or i=="u" or i=="i" or x==True:
    start=start+i
    x=True
  else:
    end=end+i
newWord=start+end+"ay"
print(newWord)