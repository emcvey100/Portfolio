import random
def __main__():
  #jokes
  jokes = [
          "Why did the physics teacher break up with the biology teacher?",
          "Why do the French like to eat snails so much?",
          "Husband: Oh the weather is lovely today. Shall we go out for a quick jog?",
          "A guest calls the waiter and complains, 'How come there are no chairs at our table?'!"
          ]
  responses = [
              "There was no chemistry.",
              "They can’t stand fast food.",
              "Wife: Hahaha, I love the way you pronounce Shall we go out and have a cake!",
              "The waiter shrugs, 'I’m sorry but you only booked one table…'"
              ]
  print ("Welcome to the tell-a-joker?")
  joke = "Yes"
  _loop_(responses, joke, jokes)

def _loop_(responses, joke, jokes):
  joke = joke.lower()
  if joke == "y" or joke == "yes":
    outjoke = random.randint(1,4)
    print (jokes[outjoke - 1])
    input("")
    print("\033[1;32;40m ",responses[outjoke - 1])
    __DYWAG_(responses, joke, jokes)
  else:
    print("\033[0; Goodbye! I hope you enjoyed the jokes.")
 

def __DYWAG_(responses, joke, jokes):
  joke = input("Do you want another joke? y/n")
  _loop_(responses, joke, jokes)

__main__()