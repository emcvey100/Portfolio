def do_calculation():
    print("lets " + command + " some numbers")
    input1 = input("Number 1>")
    input2 = input("Number 2>")
    number1 = int(input1)
    number2 = int(input2)
    if command == "add":
        result = number1 + number2
    elif command == "subtract":
        result = number1 - number2
    output = str(result)
    if command == "add":
        print(input1 + " + " + input2 + " = " + output)
    elif command == "subtract":
        print(input1 + " - " + input2 + " = " + output)


def total():
    num=int(input("How many numbers?"))
    total=0
    for i in range(num):
        total+=int(input("Number:"))


print("Hi, I am Marvin, your personal bot.")
#gets what the user wants
finished = False

while finished == False:

    command = input("How can I help? ")
    if command == "add":
        do_calculation()
    elif command == "total":
        total()
    elif command == "subtract":
        do_calculation()
    elif command == "bye":
        finished = True
    elif command == "divide":
        #if wanted to divide then divide two numbers
        print("lets divide some numbers")
        input1 = input("Number 1> ")
        input2 = input("Number 2> ")
        number1 = int(input1)
        number2 = int(input2)
        result = number1 / number2
        output = str(result)
        print(input1 + " / " + input2 + " = " + output)
    elif command == "multiply":
        #if wanted to multiply then multiply two numbers
        print("lets multiply some numbers")
        input1 = input("Number 1> ")
        input2 = input("Number 2> ")
        number1 = int(input1)
        number2 = int(input2)
        result = number1 * number2
        output = str(result)
        print(input1 + " * " + input2 + " = " + output)
    elif command == "average":
        how_many = input("How many numbers> ")
        how_many = int(how_many)
        total = 0
        for number_count in range(how_many):
            number = input("Enter number " + str(number_count) + "> ")
            total = total + int(number)
        result = total / how_many
        print("the average = " + str(result))

    elif command == "shopping list":
        shopping = []
        how_many = input("how many items of shopping do you have? ")
        how_many = int(how_many)

        for item_number in range(how_many):
            item = input("what is item number " + str(item_number) + "? ")
            shopping.append(item)

        print(shopping)
        for item in shopping:
            print(item)
            count = count + 1

        print(count)
        print(len(shopping))
    elif command == "add shopping":
        how_many = input("how many items of shopping do you have? ")
        how_many = int(how_many)
        amount=0
        for item_number in range(how_many):
            amount+=int(input("price of item"))
        print(amount)
    else:
        #users wanted was not there
        print("sorry I dont understand")
