import random
from hangman_art import logo, stages
from hangman_words import word_list
import os

lives = 6
chosen_word = random.choice(word_list)
displayed_list = ["_"] * len(chosen_word)
is_complete = False

print(logo)
print(f"The chosen word is {chosen_word}")

while lives > 0 and not is_complete:
  letter_guessed = input("Please guess a letter: ")

  os.system('cls')

  print(logo)
  print(f"The chosen word is {chosen_word}")
  
  if len(letter_guessed) != 1:
    print("Please guess exactly 1 letter at a time!")
    continue
  
  if letter_guessed in chosen_word:
    if letter_guessed not in displayed_list:
      print(f"Your guess is correct! The letter {letter_guessed} appears in the following positions:")
    else:
      print(f"Woops. It appears that you have guessed this letter {letter_guessed} before!")
    for i, letter in enumerate(chosen_word):
      if letter == letter_guessed:
        displayed_list[i] = letter_guessed
    
    if "_" not in displayed_list:
      is_complete = True

    print(" ".join(displayed_list))
  else:
    lives -= 1
    print("Your guess is incorrect. You have lost 1 life! Don't let it reach 0!")
    print(f"Number of lives left: {lives}")

  print(stages[lives])

if is_complete:
  print("Congratulations!!!!")
