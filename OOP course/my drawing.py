from Shapes import Triangle, Rectangle, Oval

rect1=Rectangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")

rect2=Rectangle()

rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")

rect2.set_x(100)
rect2.set_y(100)

oval1=Oval()

oval1.randomize()

tri = Triangle(5, 5, 100, 5, 100, 200)


tri.draw()
rect1.draw()
rect2.draw()
oval1.draw()
