myStack = [" Abid ", "Sam ", " ", " ", " ", " ", " "]

StackPointer = 2 
Max = 6 # Max is the maximum number of Stack elements

def push():
    global Max
    global StackPointer

    if StackPointer ==Max:
        print("Stack is full")
    else:
        data = input("enter name  ")
        myStack[StackPointer] = data
        StackPointer = StackPointer+1

      
def pop():
    global StackPointer
    global Max

    if StackPointer ==0:
        print("Stack is empty")
    
    else:
        data = myStack[StackPointer]
        print("You Read " + str(data))
        StackPointer = StackPointer -1
               
        
#CONT = True  
#while CONT:
print (myStack)
push()  # use pop or push to read from or add to stack.
print (myStack)
