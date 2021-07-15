import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state name?").title()

if answer_state in states_list:
    print("Correct")
else:
    print("Incorrect")