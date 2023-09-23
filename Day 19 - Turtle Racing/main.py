from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, enter a color ")
colors = ['red','orange','yellow','green','blue','indigo','violet']
y_positions = [-120,-80,-40,0,40,80,120]
turtles = []
race_on = False

for i in range(7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-280, y=y_positions[i])
    turtles.append(new_turtle)

if user_choice:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 270:
            race_on = False
            turtle_color = turtle.pencolor()
            if turtle_color == user_choice:
                print(f"you won. The {turtle_color} turtle won the race")
                turtle.write("You won!", align="right", font=("Cooper Black", 25, "italic"))
            else:
                print(f"You lost. The {turtle_color} turtle won the race")
                turtle.write("You lose!", align="right", font=("Cooper Black", 25, "italic"))
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()