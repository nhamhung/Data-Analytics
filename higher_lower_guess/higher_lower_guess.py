from game_data import data
from art import logo, vs
import random
from os import system

A = random.choice(data)
B = random.choice(data)
current_score = 0
is_game_over = False

def compare(A, B):
  return 'A' if A['follower_count'] > B['follower_count'] else 'B'

while not is_game_over:
  print(logo)
  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

  user_input = input("Who has more followers? Type 'A' or 'B': ")
  print(A['follower_count'], B['follower_count'])

  if user_input == compare(A, B):
    system('cls')
    current_score += 1
    print(f"You are right! Current score: {current_score}.")
    A = B
    B = random.choice(data)
  else:
    print(f"Sorry that's wrong. Final score: {current_score}")
    is_game_over = True
