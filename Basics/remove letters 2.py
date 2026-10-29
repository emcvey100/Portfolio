#Given a string and an integer n, write a function that removes characters from string starting from zero up to n and return a new string.
#Note: n must be less than length of string
#For exaple, removeChars("pynative",4) so output must be tive
word = input("Please, type a word:")
n=len(word)
while n > len(word)-1:
    n = int(input("How many numbers do you want to remove"))
new = ""
for i in range (n, len(word)):
    new= new + word[i]
print(new)
