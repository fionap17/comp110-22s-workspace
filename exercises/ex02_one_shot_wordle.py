"""Ex02 - wordle, guessing game obession."""

__author__ = "730243735"

SECRET_WORD = str("python")
guess: str = str(input("what is your 6-letter guess?"))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
s: str = str("")

while len(guess) < len(SECRET_WORD) or len(guess) > len(SECRET_WORD):
    guess: str = str(input("That was not 6 letters. try again:"))
else:
    while index < len(SECRET_WORD):
        if guess[index] == SECRET_WORD[index]:
            s = s + GREEN_BOX
        else:
            s = s + WHITE_BOX
        index = index + 1
print(s)
if guess == SECRET_WORD:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")