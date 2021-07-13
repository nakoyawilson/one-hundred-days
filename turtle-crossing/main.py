import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
cars.create_car()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(cars.car_speed)
    screen.update()

    cars.move()

    if player.ycor() > FINISH_LINE_Y:
        player.level_up()
        cars.change_speed()

    if cars.xcor() < -300:
        cars.create_car()