from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setposition(0, 270)
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", True, align="center", font=("Menlo", 20, "normal"))
        self.goto(0, 270)

    def update_score(self):
        self.score += 1
        self.clear()

