from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")

# Create starting snake
starting_x = 0
starting_y = 0
snake_length = 0
while snake_length < 3:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(starting_x, starting_y)
    snake_length += 1
    starting_x -= 20

screen.exitonclick()