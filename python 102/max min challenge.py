from random import randint
total = 0
max=0
min=1000
for i in range(50):
    num=randint(1,100)
    total+=num
    if num>max:
        max=num
    elif num<max:
        min=num
avg=total/50
