def circle_area(r):
  return 3.14 * r * r

def circle_circumference(r):
  return 3.14 * 2 * r

def rect_area(base, height):
    return base*height

def per_rect(base,height):
    return (base*2)+(height*2)

from turtle import Turtle

em = Turtle()

def draw_circle(t_name, r, col):
  t_name.color(col)
  t_name.dot(2 * r)
  
  t_name.penup()
  t_name.goto(0,5) #Assumes circle is at 0,0. How might you adapt if you have x,y parameters?
  t_name.pendown()
  t_name.color("black")
  t_name.write("Area: " + str(circle_area(r)), align="center")
  
  t_name.penup()
  t_name.goto(0,-5)
  t_name.pendown()
  t_name.color("black")
  t_name.write("Circumference: " + str(circle_circumference(r)), align="center")

draw_circle(em, 15, "blue")

def draw_rect(t_name, base, height, col):
    t_name.color(col)
    t_name.begin_fill()
    t_name.forward(base)
    t_name.right(90)
    t_name.forward(height)
    t_name.right(90)
    t_name.forward(base)
    t_name.right(90)
    t_name.forward(height)
    t_name.right(90)
    t_name.end_fill()

    t_name.penup()
    t_name.goto(0,5) 
    t_name.pendown()
    t_name.color("black")
    t_name.write("Area: " + str(rect_area(base,height)), align="center")
      
    t_name.penup()
    t_name.goto(0,-5)
    t_name.pendown()
    t_name.color("black")
    t_name.write("Perimeter: " + str(per_rect(base,height)), align="center")
        
