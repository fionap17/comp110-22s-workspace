"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730243735"

chosen_word: str = input("Enter a 5-character word:")
if len(chosen_word) != 5:
    print("Error: word must contain 5 characters")
    exit()
else:
    chosen_letter: str = input("Enter a single character:")
    if len(chosen_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + chosen_letter + " in " + chosen_word)
        char1: str = chosen_word[0]
        char2: str = chosen_word[1]
        char3: str = chosen_word[2]
        char4: str = chosen_word[3]
        char5: str = chosen_word[4]
        count: int = 0
        if char1 == chosen_letter:
            print(chosen_letter + " found at index 0")
            count = count + 1
        if char2 == chosen_letter:
            print(chosen_letter + " found at index 1")
            count = count + 1
        if char3 == chosen_letter:
            print(chosen_letter + " found at index 2")
            count = count + 1
        if char4 == chosen_letter:
            print(chosen_letter + " found at index 3")
            count = count + 1
        if char5 == chosen_letter:
            print(chosen_letter + " found at index 4")
            count = count + 1
        if count == 1: 
            print("1 instance of " + chosen_letter + " found in " + chosen_word)
        if count >= 2:
            print(str(count) + " instances of " + chosen_letter + " found in " + chosen_word)
        if count == 0:
            print("No instances of " + chosen_letter + " found in " + chosen_word)