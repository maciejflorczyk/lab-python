from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 22, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.color("white")  # if using a dark background
        self.goto(0, 270)  # top center
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_left} : {self.score_right}", align=ALIGNMENT, font=FONT)

    def increase_score_left(self):
        self.clear()
        self.score_left += 1
        self.update_scoreboard()

    def increase_score_right(self):
        self.clear()
        self.score_right += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)  # top center
        self.color("red")
        self.write("Game Over!", align=ALIGNMENT, font=FONT)