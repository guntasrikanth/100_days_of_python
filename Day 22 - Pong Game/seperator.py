from turtle import Turtle


class Seperator:
    def __init__(self):
        dot = Turtle('turtle')
        # dot.color('white')
        dot.goto(0, 300)
        dot.right(90)
        dot.hideturtle()
        dot.pensize(width=3)

        for i in range(30):
            dot.forward(10)
            dot.color('white')
            dot.forward(10)
            dot.color('black')
