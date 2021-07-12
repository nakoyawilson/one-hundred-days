from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("A Game of Pong")
screen.tracer(0)

right_paddle = Paddle(x_start=350, y_start=0)
left_paddle = Paddle(x_start=-350, y_start=0)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 70 and ball.xcor() > 320 or ball.distance(left_paddle) < 70 and ball.xcor() < -320:
        ball.paddle_bounce()

    elif ball.xcor() > 320 or ball.xcor() < -320:
        ball.home()
        ball.opposite_start()



screen.exitonclick()