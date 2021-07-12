from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90

class Paddle(Turtle):

    def __init__(self, x_start, y_start):
        super().__init__()
        self.starting_x = x_start
        self.starting_y = y_start
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setheading(UP)
        self.goto(self.starting_x, self.starting_y)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)
