from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
