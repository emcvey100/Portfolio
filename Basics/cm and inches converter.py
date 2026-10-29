#Write a program that converts between centimetres and inches and vice versa, by:
#-asking the user to input a number
#-asking the user to choose between converting from centimetres to inches or from inches to centimetres
#-calculating and outputtin the result using fuctions

def __main__():
    #asks the user
    number = int(input("Number"))
    choice = input("""Please input 1 or 2 for the following options:
                        1) cm to inches
                        2)inches to cm""")
    #gets results
    if choice == "1":
        result=cm_to_inches(number)
    else:
        result=inches_to_cm(number)
    print(result)

def cm_to_inches(cm):
    #calcs cms to inches
    return cm * 0.393700787

def inches_to_cm(inch):
    #calcs inches to cms
    return inch * 2.54
