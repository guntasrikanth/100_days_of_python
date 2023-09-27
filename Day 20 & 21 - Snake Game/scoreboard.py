from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=('Arial', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()