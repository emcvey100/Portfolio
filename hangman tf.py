import random
word_list = ["pink", "library", "book", "red", "graph", "leg", "computer", "python"]
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')

# Randomly choose a word and make letters list
chosen_word = random.choice(word_list)
letters = ""
for i in chosen_word:
    letters = letters + "_"
lives = 6
guessed_letters = []

while lives > 6:
    # Ask user to guess a letter (make lower case) check not guessed before
    new_guess = True
    while new_guess:
        guess = input("Please guess a letter")
        new_guess = False
        for i in guessed_letters:
            if guess == i:
                print("You have already guessed")
                new_guess = True
    guessed_letter.append(guess)
    # check if letter is in word
    for i in range(len(chosenword)):
        if chosenword[i] == guess:
            letters[i] = guess
            
    
    
