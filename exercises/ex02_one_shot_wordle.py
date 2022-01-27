"""Ex02 - wordle, guessing game obession."""

__author__ = "730243735"

SECRET_WORD = str("python")
guess: str = str(input("what is your 6-letter guess?"))

while len(guess) < len(SECRET_WORD) or len(guess) > len(SECRET_WORD):
    guess: str = str(input("That was not 6 letters. try again:"))
else:
    char1 = guess[0]
    char2 = guess[1]
    char3 = guess[2]
    char4 = guess[3]
    char5 = guess[4]
    char6 = guess[5]
    while char1 != SECRET_WORD[0]:
        guess: str = str(input("Not quite. Try again:"))
    else:
        print("yay")