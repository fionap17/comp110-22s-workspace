name: str = input("What is your name?")
date: list[str] = []
if name == "chris":
    print("hi ^-^")
    item1: str = input("what is the third letter in the alphabet?")
    while item1 != "c":
        item1: str = input("what is the third letter in the alphabet?")
    if item1 == "c":
        date.append(item1)
        print(" C if deez nuts fit, you nerd.")
        print("and continually...")
        item2: str = input("what is the article you use before a word that starts with a vowel?")
        while item2 != "an":
            print("no -.-")
            print("might wanna try 1st grade again.")
            item2: str = input("what is the article you use before a word that starts with a vowel?")
        if item2 == "an":
            date.append(item2)
            print("wow, glad you know English.")
            print("Fill in the missing word of this lyric.")
            item3: str = input("I've got the __ of the tiger.")
            while item3 != "eye":
                print("well thats not how the song goes >:()")
                item3: str = input("I've got the __ of the tiger.")
            if item3 == "eye":
                date.append(item3)
                print("nice. you are cultured.")
                item4: str = input("___ me your aphrodite, make me your one and only.")
                while item4 != "make":
                    print("why did you not pay attention to me last night when we talked about the song :()")
                    print("Just say you hate me and move on.")
                    item5: str = input("___ me your aphrodite, make me your one and only.")
                if item4 == "make":
                    date.append(item4)
                    print("awhh you remembered from our text uwu")
                    item5: str = input("its the party in the ___.")
                    while item5 != "usa":
                        print("bruh, this song is iconic. how do you not know it???")
                        item5: str = input("its the party in the ___.")
                    if item5 == "usa":
                        date.append(item5[0])
                        date.append(item5[1])
                        item6: str = input("what is the opposite of on?")
                        while item6 != "off":
                            print("you've have got to be joking.")
                            item6: str = input("what is the opposite of on?")
                        if item6 == "off":
                            date.append(item6)
                            item7: str = input("what are the first two letters of the word for a sweet frozen creamy dessert?")
                            while item7 != "ic":
                                print("bruh. ben and jerry's is this. comne on now.")
                                item7: str = input("what are the first two letters of the word for a sweet frozen creamy dessert?")
                            if item7 == "ic":
                                date.append(item7)
                                print("oop, not the ick. grody")
                                item8: str = input("it is always me, myself, and ___")
                                while item8 != "i":
                                    print("-.-")
                                    print("do you live under a rock?")
                                    item8: str = input("it is always me, myself, and ___")
                                if item8 == "i":
                                    date.append(item8)
                                    print("i c u p")
                                    item9: str = input("are you taking a L?")
                                    while item9 != "yes":
                                        print("you sure about that?")
                                        item9: str = input("are you taking a L?")
                                    if item9 == "yes":
                                        item11: str = "a L"
                                        date.append(item11)
                                        print("lol loser")
                                        item10: str = "?"
                                        date.append(item10)
                                        print(date)
                                        question: str = input("Will you be my boyfriend AND Chris? yes or no: ")
                                        while question != "yes":
                                            print("will you please reconsider?")
                                            question: str = input("Will you be my boyfriend AND Chris? yes or no: ")
                                        if question == "yes":
                                            print("yay ^-^")
                                            print("march 28 <3")
else:
    print("You are sus.")