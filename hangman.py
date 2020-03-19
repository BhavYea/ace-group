# importing the time module
#import time

wordlist = ["fixable","glowworm","numbskull","whomever","quizzes"] # * Add more words in this list
word_i = iter(wordlist)

while True:
    word = next(word_i)

    # creates an variable with an empty value
    guesses = ''

    # determine the number of tries
    tries = 10

    # Create a while loop

    # check if the tries are more than zero
    while 1:

        # make a counter that starts with zero
        failed = 0

        # for every character in secret_word
        for char in word:

            # see if the character is in the players guess
            if char in guesses:

                # print then out the character
                print(char, end="")

            else:

                # if not found, print a dash
                print("_", end="")

            # and increase the failed counter with one
                failed += 1

        # if failed is equal to zero

        # print You Won
        if failed == 0:
            print("\nYou won")

        # exit the script
            break

        # ask the user go guess a character
        guess = input("\nguess a character:")

        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        if guess not in word:

            # tries counter decreases with 1 (now 9)
            tries -= 1

        # print wrong
            print("\nWrong")

        # how many tries are left
            print("\nYou have", + tries, 'more guesses')

        # if the tries are equal to zero
            if tries == 0:

                # print "You Lose"
                print("\nYou Lose")
                break
    again = input("Want to try again?\n")
    # print("         =>",again)
    if(again == "no"):
        print("Thanks for playing")
        break
