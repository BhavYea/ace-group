import random   # ? for picking random word

wordlist = ["fixable", "glowworm", "numbskull",
            "whomever", "quizzes"]  # * Add more words in this list


def checkSingle(param):
    if(len(param) > 1):
        return 1
    else:
        return 0


def checkChar(char, guesses, left):
    if char in guesses:
        print(char, end="")
    else:
        print("_", end="")
        left += 1
    return left     # Number of Characters still left to guess


while True:
    # // word = next(word_i)
    # word = random.choice(wordlist)
    word = "thisword"
    guesses = ''
    tries = 10

    while True:
        left = 0
        for char in word:
            left = checkChar(char, guesses, left)

        # if failed is equal to zero print You Won
        if left == 0:
            print("\nYou won")
            break

    # if printGuessed(word, guesses) == 0:
    #     print("You won")

        # ask the user go guess a character
        guess = input("\nGuess a character:")
        while checkSingle(guess) == 1:
            if(checkSingle(guess) == 1):
                print("\nEnter only one character at a time")
                guess = input("\nguess a character:")

        guesses += guess
        if guess not in word:
            tries -= 1
            print("\nWrong")
            print("\nYou have", + tries, 'more guesses')

            if tries == 0:
                print("\nYou Lose")
                break
    again = input("Want to try again?\n")
    if(again == "no"):
        print("Thanks for playing")
        break
