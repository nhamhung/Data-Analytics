from turtle import Turtle

LEFT_POSITION = (-150, 200)
RIGHT_POSITION = (100, 200)
FONT = ("Arial", 60, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_both()

    def write_score(self, position, score):
        self.goto(position)
        self.write(f"{score}", font=FONT)

    def write_both(self):
        self.clear()
        self.write_score(LEFT_POSITION, self.l_score)
        self.write_score(RIGHT_POSITION, self.r_score)

    def left_score(self):
        self.l_score += 1
        self.write_both()

    def right_score(self):
        self.r_score += 1
        self.write_both()