#Write a program that accepts a string from the user and display only those characters which are present at an even index
#For example str = "pynative" so you should display 'p', 'n', 't', 'v'
word = input("Please, write a word:")
for i in range (0,len(word),2):
    print(word[i])
