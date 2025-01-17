"""Ex02 - wordle, guessing game obession."""

__author__ = "730243735"

SECRET_WORD = str("python")
word_length: str = str(len(SECRET_WORD))
guess: str = str(input(f"what is your { word_length }-letter guess?"))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
idx: int = 0
s: str = str("")

while len(guess) < len(SECRET_WORD) or len(guess) > len(SECRET_WORD):
    guess = str(input(f"That was not { word_length } letters. try again:"))
else:
    while idx < len(SECRET_WORD):
        if guess[idx] == SECRET_WORD[idx]:
            s = s + GREEN_BOX
        else:
            var: bool = False
            alt_idx: int = 0
            while not var and alt_idx < len(SECRET_WORD):
                if guess[idx] == SECRET_WORD[alt_idx]:
                    var = True
                alt_idx = alt_idx + 1
            if var:
                s = s + YELLOW_BOX
            else:
                s = s + WHITE_BOX
        idx = idx + 1
print(s)
if guess == SECRET_WORD:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")