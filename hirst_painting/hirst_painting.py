import colorgram
import turtle as t
import random

colors = colorgram.extract('hirst.jpg', 30)

rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

rgb_colors = rgb_colors[3:]
t.colormode(255)
tim = t.Turtle()
tim.hideturtle()
tim.speed("fastest")

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for i in range(1, number_of_dots + 1):
    tim.pendown()
    tim.dot(20, random.choice(rgb_colors))
    tim.penup()
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()