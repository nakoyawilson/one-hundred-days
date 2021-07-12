from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90

class Paddle:

    def __init__(self, x_start, y_start):
        self.starting_x = x_start
        self.starting_y = y_start
        self.paddle = self.create_paddle(self.starting_x, self.starting_y)

    def create_paddle(self, starting_x, starting_y):
        paddle = Turtle(shape="square")
        paddle.color("white")
        paddle.shapesize(stretch_len=5, stretch_wid=1)
        paddle.penup()
        paddle.setheading(UP)
        paddle.goto(starting_x, starting_y)
        return paddle

    def up(self):
        self.paddle.forward(MOVE_DISTANCE)

    def down(self):
        self.paddle.backward(MOVE_DISTANCE)
