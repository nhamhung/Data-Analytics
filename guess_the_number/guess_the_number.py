from art import logo
import random
import os


def play():
    random_number = random.randint(1, 100)
    num_attempts = None

    print("I'm thinking of a number between 1 and 100")

    game_mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if game_mode == 'easy':
        num_attempts = 10
    elif game_mode == 'hard':
        num_attempts = 5
    else:
        num_attempts = 10
        print(
            "Your input format was not correct... You will get the 'easy' mode by default!")

    while num_attempts > 0:
        print(f"You have {num_attempts} remaining guesses of the number.")
        user_input = int(input("Make a guess: "))
        print(f"You have guessed {user_input}")
        if user_input > random_number:
            print("Too high")
            print("Guess again")
            num_attempts -= 1
        elif user_input < random_number:
            print("Too low")
            print("Guess again")
            num_attempts -= 1
        else:
            print("You got it!")
            break

    if num_attempts == 0:
        print("So sad! You lost the game :(")
        print(f"The number is {random_number}")


def prompt():
    os.system('cls')
    print(logo)
    print("Welcome to the Number Guessing Game!")


while input("Play the game? Type 'y' or 'n': ") == 'y':
    prompt()
    play()
