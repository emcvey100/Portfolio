#A gardener needs to buy some turf for a project they are working on. The garden is rectangular with a circular flower bed in the middle.
#Write a program that:
#-asks the user for the dimensions of the lawn and the radius of the circle(in metres)
#-uses a function to caculate and output the amount of turf needed

import math
def __main__():
    #inputs
    width=int(input("Width:"))
    length=int(input("Length:"))
    radius=int(input("Radius:"))
    #output
    print(calc(width, length, radius))
def calc(w,l,r):
    #calulations
    lawn = w*l
    bed = math.pi*r*r
    return lawn - bed
    
