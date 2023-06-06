
import random

def count(maxs, scores):
    tens = 0    

    for score in scores:
      if score == maxs:
        tens += 1
    return tens

scores = []

for x in range (0, 30):
  scores.append(random.randint(0, 10))

print(scores)

top_scorers = count(10, scores) # Count function called here

print("{0} learners got top marks".format(top_scorers))

import matplotlib.pyplot as plot
 

plot.bar(range(30),scores, align='center', alpha=0.5)

plot.xticks(range(11))
plot.ylabel('Score frequency')
plot.title('Scores on a quiz')

plot.show()
plot.savefig(fname="Quiz Chart.png")
