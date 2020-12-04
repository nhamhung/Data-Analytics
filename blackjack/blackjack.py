cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo
from replit import clear


def deal_card(card_list):
    random_card = random.choice(card_list)
    return random_card


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(card_list):
    if len(card_list) == 2 and 10 in card_list and 11 in card_list:
        return 0
    elif 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'draw'
    elif computer_score == 0:
        return 'user loses'
    elif user_score == 0:
        return 'user wins'
    elif user_score > 21:
        return 'user loses'
    elif computer_score > 21:
        return 'computer loses'
    else:
        return 'computer loses' if user_score > computer_score else 'user loses'


# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

while True:
    user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if user_input == 'y':
        pass
    else:
        break

    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while True:
        clear()
        print(logo)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0:
            print("You got a Blackjack and won!")
            break
        elif user_score > 21:
            print("You score went over 21, you lost :(")
            break
        elif computer_score == 0:
            print("Computer got a blackjack, the computer won :(")

        user_input = input("Type 'y' to get another card, type 'n' to pass: ")

        if user_input == 'y':
            clear()
            user_cards.append(deal_card(cards))
            user_score = calculate_score(user_cards)
        else:
            while computer_score < 17:
                computer_cards.append(deal_card(cards))
                computer_score = calculate_score(computer_cards)
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            print(f"Computer final hand: {computer_cards}, final score: {computer_score}")
            print(compare(user_score, computer_score))
            break
