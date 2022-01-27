"""Ex02 - wordle, guessing game obession."""

__author__ = "730243735"

SECRET_WORD = str("python")
guess: str = str(input("what is your 6-letter guess?"))

while len(guess) == 6:
    char1 = guess[0]
    char2 = guess[1]
    char3 = guess[2]
    char4 = guess[3]
    char5 = guess[4]
    char6 = guess[5]
    while char1 == SECRET_WORD[0]:
        while char2 == SECRET_WORD[1]:
            while char3 == SECRET_WORD[2]:
                while char4 == SECRET_WORD[3]:
                    while char5 == SECRET_WORD[4]:
                        while char6 == SECRET_WORD[5]:
                            print("Woo! You got it")
                    else:
                        print("Not quite.Play again soon!")
                else:
                    print("Not quite.Play again soon!")
            else:
                print("Not quite.Play again soon!")
        else:
            print("Not quite.Play again soon!")
    else:
        print("Not quite.Play again soon!")
else:
    print("That was not 6 letters! Try again:")
