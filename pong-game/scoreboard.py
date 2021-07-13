from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
SMALLER_FONT = ("Courier", 36, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.determine_winner()

    def determine_winner(self):
        if self.right_score == 11:
            self.goto(0, -100)
            self.write("Right Player is the winner!", align=ALIGNMENT, font=SMALLER_FONT)
        else:
            self.goto(0, -100)
            self.write("Left Player is the winner!", align=ALIGNMENT, font=SMALLER_FONT)
