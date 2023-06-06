import matplotlib.pyplot as plot
 
performance = [2,0,2,3,2,4,5,3,2,4,3]

plot.bar(range(11), performance, align='center', alpha=0.5)

plot.xticks(range(11))
plot.ylabel('Score frequency')
plot.title('Scores on a quiz')

plot.show()
plot.savefig(fname="Quiz Chart.png")
