from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def create_turtle(turtle_colour):
    turtle = Turtle(shape="turtle")
    turtle.color(turtle_colour)
    turtle.penup()
    return turtle

starting_x = -230
starting_y = -145
turtle_racers = []
for colour in colours:
    colour = create_turtle(colour)
    colour.goto(x=starting_x, y=starting_y)
    starting_y += 50
    turtle_racers.append(colour)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in turtle_racers:
        if racer.xcor() > 230:
            is_race_on = False
            winning_colour = racer.pencolor()
            if winning_colour == user_bet.lower():
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_colour} turtle is the winner!")
        random_distance = random.randint(0, 10)
        racer.forward(random_distance)


screen.exitonclick()