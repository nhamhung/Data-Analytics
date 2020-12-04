from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

STARTING_POSITION = [(350, 0), (-350, 0)]

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

paddle_l = Paddle(STARTING_POSITION[1])
paddle_r = Paddle(STARTING_POSITION[0])
ball = Ball()
score_board = Scoreboard()

screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_cars()

    if abs(ball.ycor()) > 270:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 330 or ball.distance(paddle_l) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        score_board.left_score()
        ball.reset_position()

    if ball.xcor() < -380:
        score_board.right_score()
        ball.reset_position()


screen.exitonclick()
