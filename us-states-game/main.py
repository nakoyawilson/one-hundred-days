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
correct_guesses = []
score = 0
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Name a state:").title()
    if answer_state in states_list:
        if answer_state in correct_guesses:
            print("Already guessed")
        else:
            state = states_data[states_data.state == answer_state]
            x_coordinate = int(state.x.to_string(index=False))
            y_coordinate = int(state.y.to_string(index=False))
            answer.goto(x_coordinate, y_coordinate)
            answer.write(f"{answer_state}", align="center", font=("Menlo", 10, "normal"))
            correct_guesses.append(answer_state)
    score = len(correct_guesses)
    if score == 50:
        answer.goto(0, 0)
        answer.write("Congratulations! You named all 50 states.", align="center", font=("Menlo", 22, "normal"))
        game_is_on = False

screen.exitonclick()