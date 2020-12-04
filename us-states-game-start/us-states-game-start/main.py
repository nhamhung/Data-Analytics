import pandas as pd
from turtle import Screen, Turtle

data = pd.read_csv("50_states.csv")

coordinates = [tuple(pair)[1:] for pair in data[['x', 'y']].itertuples()]
print(coordinates)
state_names = data['state'].tolist()

screen = Screen()
screen.title("U.S States Game")
screen.setup(700, 600)
screen.bgpic("blank_states_img.gif")

guessed = set()

while len(guessed) < 50:
    user_input = screen.textinput("Recall State Name", f"You've Got: {len(guessed)}/50 States").title()
    # user_input = " ".join([word[0].upper() + word[1:] for word in user_input.split(" ")])

    if user_input == 'Exit':
        break

    if user_input in state_names and user_input not in guessed:
        guessed.add(user_input)
        index = state_names.index(user_input)
        text = Turtle()
        text.penup()
        text.goto(coordinates[index])
        text.hideturtle()
        text.write(f"{user_input}")

states_not_guessed = pd.DataFrame(list(set(state_names).difference(guessed)))
print(states_not_guessed)
states_not_guessed.to_csv("states_not_guessed.csv")