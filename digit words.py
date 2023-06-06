#A digit word is a word where, after possibly removing some letters, you are left with one of the single digits: ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT or NINE.#
#For example:#
#• BOUNCE and ANNOUNCE are digit words, since they contain the digit ONE.#
#• ENCODE is not a digit word, even though it contains an O, N and E, since they are not in order.#
# #
#Write a program with GUI, using TKINTER,  which allows a user to input a word, and outputs if the word is digit word or not. You must use GUI so that the word will be entered in an entry box and result will show on a message box. #
def digit_words(word):
  global n
  word=word.upper()
  digit=False
  n=0

  while n<9 and digit==False:
    search=Numbers[n]
    length=len(search)-1
    searchletter=search[0]
    numbersearch=0
    for i in word:
      searchletter=search[numbersearch]
      if i == searchletter:
        if length>numbersearch:
          numbersearch=numbersearch+1
        else:
          digit=True

    n=n+1
  return digit
n=0
Numbers=[ "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
inputs=input("Word")
print (digit_words(inputs))
print(n)