def area_triangle(base,height):
    area=base*height*0.5
    return area

def reverse(string):
    new=""
    word=len(string)
    for i in range(word):
        new+=string[word]
        word+=-1
    return new

def dice():
    import random
    number=random.randint(1,6)
    return number
