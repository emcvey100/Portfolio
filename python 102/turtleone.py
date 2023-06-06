import random
from turtle import Turtle

em = Turtle()

def draw_circle(t_name, r, col):
  t_name.color(col)
  t_name.dot(r*2)
  
def draw_rect(l,h,col):
    em.color(col)
    em.hideturtle()
    length=l
    height=h
    em.begin_fill()
    em.forward(length)
    em.right(90)
    em.forward(height)
    em.right(90)
    em.forward(length)
    em.right(90)
    em.forward(height)
    em.right(90)
    em.end_fill()
    
draw_circle(em, 150, "blue")
draw_circle(em, 100, "red")
draw_circle(em, 50, "yellow")

em.shape('turtle')
em.penup()
em.goto(-160,100)
em.pendown()

draw_rect(133,78,"blue")

