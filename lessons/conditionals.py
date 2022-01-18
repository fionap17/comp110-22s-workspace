"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I am thinking of a number between 1-5, what is it?")
guess: int = int(input("what is your guess?"))

if guess == SECRET:
    print("you guessed correctly!!")
    print("Have a wonderful day!")
else: 
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("you guessed too low.")

print("Game over.")