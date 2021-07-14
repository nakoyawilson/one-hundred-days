import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, Speed
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = []
speed = Speed()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(speed.car_speed)
    screen.update()
    scoreboard.update_level()

    for i in range(1_000):
        if i == 999:
            car_manager.append(CarManager())

    for car in car_manager:
        car.move()

        # Detect collision with car
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > FINISH_LINE_Y:
        player.level_up()
        speed.change_speed()
        scoreboard.increase_level()


screen.exitonclick()