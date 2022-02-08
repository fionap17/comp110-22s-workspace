"""Making an actual wordle."""

__author__ = "730243735"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, letter: str) -> bool:
    """Search for letter in word."""
    assert len(letter) == 1
    idx: int = 0
    while idx < len(word):
        if letter == word[idx]:
            return True
        idx = idx + 1
    return False


def emojified(guess: str, SECRET: str) -> str:
    """Testing for yellow or white boxes depending on return of contains_char."""
    assert len(guess) == len(SECRET)
    idx: int = 0
    s: str = ""
    while idx < len(SECRET):
        if guess[idx] == SECRET[idx]:
            s = s + GREEN_BOX
        else:
            if contains_char(SECRET, guess[idx]) is False:
                s = s + WHITE_BOX
            else:
                s = s + YELLOW_BOX
        idx = idx + 1
    return s


def input_guess(word_length: int) -> str:
    """Checks word length until it matches expected."""
    guess: str = input(f"Enter a {word_length} character word: ")
    while len(guess) < word_length or len(guess) > word_length:
        guess = input(f"That wasn't {word_length} chars! Try again: ")
    else:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    SECRET: str = "codes"
    guess: str = ""
    n: int = 1
    while guess != SECRET and n < 7:
        print(f"=== Turn {n}/6 ==")
        guess = input_guess(len(SECRET))
        print(emojified(guess, SECRET))
        if guess == SECRET:
            print(f"You won in {n}/6 turns!")
        n = n + 1
    if n == 7:
        print("X/6- Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()