from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = list(range(-125, 150, 50))
all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape='turtle')
    all_turtles.append(new_turtle)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    new_turtle.pendown()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")

        turtle.penup()
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()