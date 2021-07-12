from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("A Game of Pong")

right_paddle = Paddle(x_start=350, y_start=0)
left_paddle = Paddle(x_start=-350, y_start=0)

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


screen.exitonclick()