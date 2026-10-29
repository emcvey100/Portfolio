#Write a program that:
#-asks the user to input a number
#-outputs the times table for that number
#-starts again every time it finishes

#starts again every time it finishes
while True:
    #asks the user to input a number
    number = input("Number:")
    #outputs the times table for that number
    for i in range(13):
        print(i*number)
