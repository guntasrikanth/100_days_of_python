from turtle import Screen
import time
from seperator import Seperator
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

seperator = Seperator()
scoreboard = Scoreboard()
right_paddle = Paddle((370, 0))
left_paddle = Paddle((-370, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "u")
screen.onkey(left_paddle.down, "d")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect with top or lower edge
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect with the paddle and bounce back
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.move_speed *= 0.9
        ball.bounce_x()

    #went out of range
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_score_increase()

    if ball. xcor() < -390:
        ball.reset_position()
        scoreboard.right_score_increase()

    if scoreboard.right_score == 10:
        game_is_on = False
        scoreboard.game_over('Left player')

    if scoreboard.left_score == 10:
        game_is_on = False
        scoreboard.game_over('Right player')

screen.exitonclick()
