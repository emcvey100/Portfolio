#Write a program that:
#-asks the user to input a sentence
#-asks the user to input:
# -the word they want to replace
# -the word they want to replace it with
#-outputs the new sentence

#-asks the user to input a sentence
sentence=input("Sentence:")
#-asks the user to input:
# -the word they want to replace
word= input("Word to replace:")
# -the word they want to replace it with
word_replaced = input("Replaced word:")
#-outputs the new sentence
sentence = sentence.replace(word, word_replaced)
