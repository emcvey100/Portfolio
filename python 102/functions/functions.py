def haiku(poem):
    for i in range(3):
        print(poem[i])

def area_triangle():
    height=float(input("height:"))
    base=float(input("base:"))
    area=height*base*0.5
    print(area)

def coin_flip():
    import random
    mychoice=["heads","tails"]
    print(random.choice(mychoice))
    
