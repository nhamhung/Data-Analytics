from turtle import Turtle

MOVE_DISTANCE = 20
X_SIGN = 1
Y_SIGN = -1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto((0, 0))
        self.x_sign = X_SIGN
        self.y_sign = Y_SIGN
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + MOVE_DISTANCE * self.x_sign
        new_y = self.ycor() + MOVE_DISTANCE * self.y_sign
        self.goto((new_x, new_y))

    def bounce_y(self):
        self.y_sign *= -1

    def bounce_x(self):
        self.x_sign *= -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()