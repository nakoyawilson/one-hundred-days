import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answer = turtle.Turtle()
answer.penup()
answer.hideturtle()

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()



game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()
    if answer_state in states_list:
        state = states_data[states_data.state == answer_state]
        x_coordinate = int(state.x.to_string(index=False))
        y_coordinate = int(state.y.to_string(index=False))
        answer.goto(x_coordinate, y_coordinate)
        answer.write(f"{answer_state}", align="center", font=("Menlo", 10, "normal"))

screen.exitonclick()