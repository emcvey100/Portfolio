def fibonacci():
  start=0
  next1=1
  for i in range (0,100):
    print(start)
    next2=next1+start
    start=next1
    next1=next2
fibonacci()