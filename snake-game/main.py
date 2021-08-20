from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

def run_game():

    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Python Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:

        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.update_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset_score()
            snake.reset_snake()
            scoreboard.game_over()
            restart = screen.textinput("Do you want to play again?", "Type 'y' or 'n':")
            if restart == "y":
                screen.clearscreen()
                run_game()
            elif restart == "n":
                game_is_on = False

        else:
            # Detect collision with tail
            for segment in snake.snake_segments[1:]:
                if snake.head.distance(segment) < 10:
                    scoreboard.reset_score()
                    snake.reset_snake()
                    scoreboard.game_over()
                    restart = screen.textinput("Do you want to play again?", "Type 'y' or 'n':")
                    if restart == "y":
                        screen.clearscreen()
                        run_game()
                    elif restart == "n":
                        game_is_on = False


screen = Screen()
run_game()
screen.exitonclick()



