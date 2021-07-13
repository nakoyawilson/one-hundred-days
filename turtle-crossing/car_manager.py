from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

STARTING_X = 300

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_speed = 0.1

    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        starting_y = random.randrange(-260, 260, 20)
        self.goto(STARTING_X, starting_y)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)

    def change_speed(self):
        self.car_speed *= 0.9
