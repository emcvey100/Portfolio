#In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number
import random
def guess_game(number, guesses):
    if guesses>10:
        print("You lose!")
        return False
    else:
        guess=input("Number:")
        while len(guess) != 3 or not guess.isdecimal():
            guess=input("Number:")
        if number == guess:
            print("Bagles!")
            return False
        for i in range(3):
            if guess[i+1] == number[i+1]:
                print("Fermi")
            elif guess[i+1] in number:
                print("Pico")
        return True
def game():
    number=str(random.randint(9))+str(random.randint(9))+str(random.randint(9))
    guesses=0
    if not guess_game(number,guesses):
        inp=input('Do you want to play again? (y or n)')
        if inp == "y":
            game()
        else:
            return
game()
