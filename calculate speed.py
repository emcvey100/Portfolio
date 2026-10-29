#Write a program that:
#-asks the user for the ditance (in metres)
#-asks the user for the time in seconds that a jorney was completed in
#-calculates and outputs the average speed using a function

def __main__():
    #inputs
    number_1 = int(input("Metres:"))
    number_2 = int(input("Seconds:"))
    #outputs
    print(calc(number_1, number_2))
def calc(metre, secs):
    #calculations
    return metre/secs
    
