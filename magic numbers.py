#write a program that allow users to enter two integers and return their product. If the product is greater than 1000, then return their sum.__
number_1 = int(input("Number:"))
number_2 = int(input("Number:"))
if number_1 * number_2 >=1000:
    print(number_1+number_2)
else:
    print(number_1*number_2)
