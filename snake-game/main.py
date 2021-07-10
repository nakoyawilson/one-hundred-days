from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
snake.create_snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()