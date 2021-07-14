from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Menlo", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.display_score()