from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if self.should_create_random():
            new_car = Turtle()
            new_car.color(f"{random.choice(COLORS)}")
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            starting_x = 300
            starting_y = random.randint(-250, 250)
            new_car.goto(starting_x, starting_y)
            new_car.setheading(180)
            self.cars.append(new_car)

    def should_create_random(self):
        return random.randint(1, 6) == 1

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT