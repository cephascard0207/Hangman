# Hangman
# Created by Cephas Cardozo
# Developed using Python

# imports
import random
from hangman_logo import logo
from hangman_words import word_list

# welcome_print
print(logo)
print("\nCreated by Cephas Cardozo\nDeveloped using Python\n")

# variables
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = []

# loops_&_conditionals
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You have already guessed{guess}")

      
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, thats not in the word. You LOSE a Life! \nLIVES = {lives}\n")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

# print_statement_ACII_art
    print(stages[lives])