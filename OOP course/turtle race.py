from turtle import Turtle
from random import randint

em=Turtle()
em.color('red')
em.shape('turtle')
em.penup()
em.goto(-160,100)
em.pendown()


ben=Turtle()
ben.color('blue')
ben.shape('turtle')
ben.penup()
ben.goto(-160,70)
ben.pendown()

tom=Turtle()
tom.color('purple')
tom.shape('turtle')
tom.penup()
tom.goto(-160,40)
tom.pendown()

jeff=Turtle()
jeff.color('green')
jeff.shape('turtle')
jeff.penup()
jeff.goto(-160,10)
jeff.pendown()



for movement in range (100):
    em.forward(randint(1,5))
    ben.forward(randint(1,5))
    tom.forward(randint(1,5))
    jeff.forward(randint(1,5))
    
