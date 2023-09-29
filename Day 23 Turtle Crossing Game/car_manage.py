from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITIONS = [0, 40, 80, 120, 150, 180, -40, -80, -120, -150, -180]


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=0.5, stretch_len=1.2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT