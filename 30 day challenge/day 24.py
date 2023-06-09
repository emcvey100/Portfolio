#Write a function that takes two numbers.
#The first number indicates the number of spaces that should be displayed and the second indicate the number of Xs that should be displayed. These should both be displayed on the same line.
#Now write another function that makes multiple calls to your first function and draws a picture with Xs.

def draw_line(i,j):
    for i in range(i):
        print(" ", end="")
    for i in range(j):
        print("X", end="")
    print()

def draw_picture():
    for x in range(5):
        draw_line(x,5)
    for y in range(4, 0, -1):
        draw_line(y,4)
draw_picture()
