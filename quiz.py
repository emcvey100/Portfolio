def start():
    #welcomes the program
    print("""Quiz program
This stores question and allows you to take the test: """)
    #sets list
    Quiz=[[], []]
    awnser=[[],[]]
    #gets 2 question sets
    for i in range (2):
        Quiz[i]=makequestion(i)
        awnser[i] =answer(Quiz[i][1])
    #get score and prints it
    Score=doquiz(Quiz,awnser)
    #work out percentage
    per=str((int(Score)/2)*100)
    #output score
    print(str(Score) + "/2 which is " + per + "%!")


def makequestion(i):
  #input question asked
    Question=input("Enter question: ")
    #input the amount of questions wanting
    mAns=input("How many awnsers: ")
    #validation
    while mAns.isdigit()==False:
        mAns=input("Enter amount of awnsers: ")
    mAns=int(mAns)-1
    #return question and amount of awnsers
    return Question,mAns

def answer(nAns):
    answer=" "
    #make awnsers list
    for i in range(int(nAns)+1):
	    answer += input("Enter possible answer: ")+"#split#"
    answer=answer.split("#split#")
    #enter the correct answer
    correct=input("Which is the correct answer: ")
    #validation
    while correct.isdigit()==False:
        correct=input("Which is the correct answer: ")
    correct=int(correct)-1
    answer[len(answer)-1]=correct
    #return awnsers plus correct one
    return answer
    
def doquiz(ques,ans):
  correct=0
  #print the two sets of questions
  for i in range(2):
    #print question
        print(ques[i][0])
        #print awnsers
        for o in range (ques[i][1]+1):
            print(ans[i][o])
        #input choice
        your=input("Your answer: ")
        #validation
        while your.isdigit()==False:
          your=input("Your answer: ")
        your=int(your)-1
        num=int(ques[i][1])+1
        #check if correct or false
        if  ans[i][num]==your:
            print("Correct")
            correct+=1
        else:
            print("Wrong")
    #return the amount correct
  return correct
start()
