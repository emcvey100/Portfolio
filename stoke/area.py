#Area Calculator Python Challenge - www.101computing.net/area-calculator-python-challenge/
pi=3.1415
def __main__():
  shape=input("What shape do you want the area to? Square/Rectangle/Circle/Triangle:")
  shape = shape.lower()
  if shape == "square":
    area=_square_()
  elif shape =="rectangle":
    area=_rectangle_()
  elif shape =="circle":
    area=_circle_()
  elif shape=="triangle":
    area = _triangle_()
def _square_():
  width=int(input("width"))
  return width*width
def _rectangle_():
  width=int(input("width"))
  length=int(input(""))