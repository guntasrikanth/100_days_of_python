from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        with open('High_score.txt') as file:
            self.high_score = file.read()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}      High Score: {self.high_score}", align="center", font=('Arial', 12, 'normal'))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('High_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=('Arial', 12, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()