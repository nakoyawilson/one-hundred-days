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

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()

if answer_state in states_list:
    state = states_data[states_data.state == answer_state]
    x_coordinate = int(state.x.to_string(index=False))
    y_coordinate = int(state.y.to_string(index=False))
    print(x_coordinate)
    print(y_coordinate)
    answer.goto(x_coordinate, y_coordinate)
    answer.write(f"{answer_state}", align="center", font=("Menlo", 10, "normal"))
else:
    pass

screen.exitonclick()