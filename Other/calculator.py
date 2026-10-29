  def __main__():
    #welcoming
    print ("Welcome to to the python calculator.")
    start = "yes"
    __start__()
    #start loop to do over and over again
  def __start__():
      # numbers their
      num1 = int(input("What is your first number?"))
      num2 = int(input("What is your second number?"))
      function = input("Do you want to add, subtract, multiply, or divide?")
      function = function.lower()
      if function == "add" or function == "+":
        # +
        __plus__(num1, num2)
      elif function == "subtract" or function == "-":
        # -
        __sub__(num1, num2)
      elif function == "multiply" or function == "x" or function == "*":
        # *
        __X__(num1, num2)
      elif function == "divide" or function == "/" or function == "%":
        #/
        __div__(num1, num2)
      else:
        # go back to start
        start = "yes"

  def __plus__(num1, num2):
    print (num1, "+", num2, "=")
    anser = num1 + num2
    __loop__(anser)

  def __X__(num1, num2):
    print (num1, "x", num2, "=")
    anser = num1 * num2
    __loop__(anser)

  def __sub__(num1, num2):
    print (num1, "-", num2, "=")
    anser = num1 - num2
    __loop__(anser)

  def __div__(num1, num2):
    print (num1, "/", num2, "=")
    anser = num1 / num2
    __loop__(anser)

  def __loop__(anser):
    print (anser)
    start = input ("Do you want another calculation? y/n")
    start = start.lower()
    if start == "yes" or start == "y":
      __start__()
    else:
      __end___()

  def __end___():
    print ('Goodbye!')
  __main__()