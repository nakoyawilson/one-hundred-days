from turtle import Turtle

class Snake:

    def __init__(self):
        self.snake_segments = []

    def create_snake(self):
        starting_x = 0
        starting_y = 0
        snake_length = 0
        while snake_length < 3:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(starting_x, starting_y)
            self.snake_segments.append(snake)
            snake_length += 1
            starting_x -= 20

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.snake_segments[0].forward(20)