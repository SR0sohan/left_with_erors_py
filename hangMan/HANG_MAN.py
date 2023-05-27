import random
from hangMan.words import words
import string


def get_valid_number(words):
    word = random.choice(words)  # randomly choses something from that list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_number(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user have guessed
    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ? ' '.join('a', 'n', 'ac') -->'a n ac'
        print("you have", lives, " lives left and you have used this letters: ",
              ' '.join(used_letters))
        # ? what current word is(ie W-RD)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("current word: ", ' '.join(word_list))

        user_letter = input("guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # ! takes away a life
                print(f"letter {user_letter} is not in word.")

        elif user_letter in used_letters:
            print("you have already used that charecter.please try again")
        else:
            print("Invalid charecter.please try again!")

    #! gets here when len(word_letters)==0 or when lives == 0
    if lives == 0:
        print("you died, sorry. The word was", word)
    else:
        print("you guessed the word", word, " !!")


hangman()
