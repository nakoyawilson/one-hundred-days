from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("A Game of Pong")
screen.tracer(0)

right_paddle = Paddle(x_start=350, y_start=0)
left_paddle = Paddle(x_start=-350, y_start=0)

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()