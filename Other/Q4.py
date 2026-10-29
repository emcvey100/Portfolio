def __main__():
    word = input("Please, type a word:")
    n=len(word)
    while n > len(word)-1:
        n = int(input("How many numbers do you want to remove"))
    new = ""
    for i in range (n, len(word)):
        new= new + word[i]
    print(new)
__main__()