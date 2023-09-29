from turtle import Screen
import time
from car_manage import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.bgcolor("white")
screen.tracer(0)

car_manage = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manage.create_car()
    car_manage.move()

    if player.ycor() > 270:
        scoreboard.increase_score()
        car_manage.increase_speed()
        player.goto(0, -280)

    for car in car_manage.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
