## Guessing Game

max = 101
min = 0
n=0
print("Think of a number between 1 and 100")

def guess(max,min,count):
    middle = int((max + min)/2)
    answer = input("Is your number [H]igher, [L]ower or the [S]ame as {}".format(middle)).upper()
    if answer == "H":
      min = middle
    elif answer == "L":
      max = middle
    else:
      print("Your number is {}, it took me"+str(count)+"guess".format(middle))
      quit()
    return count+1
while True:
    n=guess(max, min, n)
