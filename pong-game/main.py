from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Python Pong")
screen.tracer(0)

right_paddle = Paddle(x_start=350, y_start=0)
left_paddle = Paddle(x_start=-350, y_start=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "e")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.change_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 70 and ball.xcor() > 320 or ball.distance(left_paddle) < 70 and ball.xcor() < -320:
        ball.paddle_bounce()

    elif ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.left_point()

    elif ball.xcor() < -380:
        ball.ball_reset()
        scoreboard.right_point()

    if scoreboard.left_score == 11 or scoreboard.right_score == 11:
        game_on = False
        scoreboard.game_over()


screen.exitonclick()