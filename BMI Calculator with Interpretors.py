height = float(input("height:"))
weight = float(input("Weight:"))

# Calculate the bmi using weight and height.
bmi = weight / (height*height)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("normal weight")
else:
    print("Overweight")
