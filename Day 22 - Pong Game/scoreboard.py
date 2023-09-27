from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-30, 240)
        self.write(arg=f"{self.left_score}", align="right", font=('Arial', 40, 'normal'))
        self.goto(60, 240)
        self.write(arg=f"{self.right_score}", align="right", font=('Arial', 40, 'normal'))

    def right_score_increase(self):
        self.right_score += 1
        self.update_scoreboard()

    def left_score_increase(self):
        self.left_score += 1
        self.update_scoreboard()

    def game_over(self, player):
        self.color('green')
        self.goto(0, 0)
        self.write(f"Game Over. {player} won!!", align="center", font=('Arial', 12, 'normal'))
