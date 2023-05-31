def InsertionSort(Lst):
    for i in range (1,len(Lst),1):
        current= Lst[i]
        extra = i
        while extra > 0 and Lst[extra-1] > current:
            Lst [extra] = Lst[extra-1]
            extra = extra -1
        Lst[extra]=current
    return Lst

def BubbleSort(lst):
    n=len(lst)
    swap=True
    while swap==True:
        swap=False
        for i in range(1, n):
            if lst[i-1]>lst[i]:
                temp=lst[i-1]
                lst[i-1]=lst[i]
                lst[i]=temp
                swap=True
        n=n-1
    return lst
def generate_list(n):
    my_list= []   # you can change the size of the list by changing the value n
    while n > 1:
        my_list.append(n)
        n -= 1
   # print ("my list was" , my_list)    # only use this line for testing your work before you start the experiment. 
    return my_list
def ExecutTime(n):
	import time

	TestList = generate_list(n)
	start1 = time.time()
	SortedList1 = BubbleSort(TestList)
	end1 = time.time()
	start2 = time.time()
	SortedList2 = InsertionSort(TestList)
	end2 = time.time()
	print("Bubble:", (end1-start1))
	print("Insertion:", (end2-start2))
	return (end1-start1) , (end2-start2)



x1=[0,0,0,0,0,0,0,0,0,0,0]
x2=[0,0,0,0,0,0,0,0,0,0,0]
y1=[500,750,1000,1500,2000,2500,3000,3500,4000,5000]
y2=y1
# lineplot.py

for i in range(10):
    n=ExecutTime(y1[i])
    x1[i]=n[0]
    x2[i]=n[1]
 # Make an array of y values for each x value
# use pylab to plot x and y
import numpy as np
import pylab as pl
pl.plot(x1, y1, 'r')
pl.plot(x2, y2, 'g')
pl.title('Plot of y vs. x')
pl.xlabel('x axis')
pl.ylabel('y axis')
pl.show() 


