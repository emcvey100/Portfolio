#Write a program that:
#-converts and outputs marks into grades, using the following data
#->=75 = A
#->=60 = B
#->=35 = C
#-<35 = D

#asks for grade
grade = input("Grade:")
#converts grade to output mark
if grade >= 75:
    print("A")
elif grade >= 60:
    print("B")
elif grade >= 35:
    print("C")
else:
    print("D")


