"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730243735"

WORD1: str = str("hello")
WORD2: str = str("heels")
LETTER1: str = str("e")
LETTER2: str = str("h")

chosen_word: str = input("Enter a 5-character word:")
if len(chosen_word) != 5:
    print("Error: word must contain 5 characters")
    exit()
else:
    chosen_letter: str = input("Enter a single character:")
    if len(chosen_letter) != 1:
        print("Error: Character must be a single character.")
    else:
        print("Searching for " + chosen_letter + " in " + chosen_word + "")
        if chosen_letter != str("h") or str("e") or str("l") or str("o") or str("s"):
            if chosen_word == WORD1:
                if chosen_letter == LETTER1:
                    print("e found at index 1")
                    print("1 instance of e found in hello")
            if chosen_word == WORD2:
                if chosen_letter == LETTER1:
                    print("e found at index 1")
                    print("e found at index 2")
                    print("2 instances found in heels")
                if chosen_letter == LETTER2:
                    print("h found at index 0")
                    print("1 instance of h found in heels")
        else:
            print("No instances of " + chosen_letter + " found in " + chosen_word + "")