from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def start_game():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


random_number = random.randint(0, 9)


@app.route("/<int:user_guess>")
def check_number(user_guess):
    if user_guess == random_number:
        return '<h1 style="color:green">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif user_guess < random_number:
        return '<h1 style="color:red">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color:orange">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'


if __name__ == "__main__":
    app.run()