# Guess secret number game, 5 lives
import random

secret_number = random.randint(1, 10)
guesses = 5

while guesses > 0:
    print("You have %s guesses left" % guesses)
    guess_input = int(input("I am thinking of a number between 1 and 10. "))

    if guess_input == secret_number:
        print("Yay you guessed right, you win no prize though!")
        break
    elif guess_input < secret_number:
        print(str(guess_input) + " is TOO LOW, try again!")
        guesses -= 1
    elif guess_input > secret_number:
        print(str(guess_input) + " is TOO HIGH, try again!")
        guesses -= 1
        
    if guesses == 0:
        print("Game over")
        guesses -= 1
        redo = input("Do you want to play again (Y or N) ")
        if redo == "Y":
            guesses = 5
        elif redo == "N":
            print("OK")