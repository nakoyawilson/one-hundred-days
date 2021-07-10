from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

# Create starting snake
starting_x = 0
starting_y = 0
snake_length = 0
segments = []
while snake_length < 3:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.penup()
    snake.goto(starting_x, starting_y)
    segments.append(snake)
    snake_length += 1
    starting_x -= 20

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(segments) - 1, 0, -1):
        new_x = segments[segment -1].xcor()
        new_y = segments[segment -1].ycor()
        segments[segment].goto(new_x, new_y)
    segments[0].forward(20)


screen.exitonclick()