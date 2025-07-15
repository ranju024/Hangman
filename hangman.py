# Problem Set 2, hangman.py
# Name: Ranju Sharma
# Collaborators: None
# Time spent: 10 hours

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for letters in secret_word:
        if letters not in letters_guessed:
          return False
    return True

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
          guessed_word = guessed_word + letter
        else:
          guessed_word += '*'
    return guessed_word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    remaining_letters = ''
    alphabets = string.ascii_lowercase
    for letter in alphabets:
        if letter not in letters_guessed:
            remaining_letters += letter
    return remaining_letters
    # return ''.join([ch for ch in string.ascii_lowercase if ch not in letters_guessed])



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """

    print(f'Welcome to Hangman!\nI am thinking of a word that is {len(secret_word)} letters long.\n------')
    no_guesses = 10
    letters_guessed = []
    vowels = ['a','e', 'i', 'o','u']
    consonants = [i for i in string.ascii_lowercase if i not in vowels]

    while True:
      available_letters = get_available_letters(letters_guessed)
      print(f'You have {no_guesses} guesses left.')
      print(f'Available letters: {available_letters}')
      guessed_letter = input("Please guess a letter: ").strip().lower()

      if guessed_letter == '!' and with_help:
        pass
      elif not guessed_letter.isalpha() or len(guessed_letter) != 1:
        print(f'Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}')
        print('------')
        continue
      unguessed_letters = [letter for letter in secret_word if letter not in letters_guessed]


      if guessed_letter == '!' and with_help:
        if unguessed_letters:
          if no_guesses < 3:
            print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
            print('------')

          else:
            revealed_letter = random.choice(unguessed_letters)
            letters_guessed.append(revealed_letter)
            no_guesses -= 3
            print(f'Letter revealed: {revealed_letter}')
            print(f'{get_word_progress(secret_word, letters_guessed)}')
            print('------')

      elif guessed_letter == '!' and not with_help:
         print("Help is not enabled.")
         continue
      
      elif guessed_letter in vowels:
        if guessed_letter in unguessed_letters:
          letters_guessed.append(guessed_letter)
          unguessed_letters.remove(guessed_letter)
          print(f'Letter revealed: {guessed_letter}')
          print(f'Good guess: {get_word_progress(secret_word, letters_guessed)}')
          print('------')
        elif guessed_letter in letters_guessed:
          print(f'Already guessed')
          print('------')
        else:
          no_guesses -= 2
          letters_guessed.append(guessed_letter)
          print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')
          print('------')
      
      elif guessed_letter in consonants:
        if guessed_letter in unguessed_letters:
          letters_guessed.append(guessed_letter)
          unguessed_letters.remove(guessed_letter)
          print(f'Letter revealed: {guessed_letter}')
          print(f'Good guess: {get_word_progress(secret_word, letters_guessed)}')
          print('------')
        elif guessed_letter in letters_guessed:
          print(f"Oops! You've already guessed that letter: {get_word_progress(secret_word, letters_guessed)}")
          print('------')
        else:
          no_guesses -= 1
          letters_guessed.append(guessed_letter)
          print(f'Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}')
          print('------')
    
      if no_guesses <= 0:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}')
        break
      
      if has_player_won(secret_word, letters_guessed):
        score = no_guesses + 4 * len(set(secret_word)) + 3 * len(secret_word)
        print(f'Congratulations, you won!\nYour total score for this game is: {score}')
        print('========')
        break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

