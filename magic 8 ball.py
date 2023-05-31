import random
responses=["It is certain",
            "Better not tell you now",
            "Out look not so good",
            "Concerntrate and ask again",
            "Yes, certainly",
            "Definely yes",
            "No",
            "Definely no",
            "Ask again another time"]
askQuestion="y"
while askQuestion=="y" or askQuestion=="yes":
  question=input ("Ask a Question:")
  print (random.choice(responses))
  askQuestion=input ("Do you want to ask another question:")
  askQuestion=askQuestion.lower()
