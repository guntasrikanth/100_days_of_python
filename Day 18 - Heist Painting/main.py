import colorgram
import turtle
import random

colors = colorgram.extract('img.jfif', 30)
rgb_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tuple = (r,g,b)
    rgb_list.append(tuple)


timmy = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
timmy.hideturtle()
timmy.penup()
timmy.speed(0)
timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)

for col in range(10):
    for row in range(10):
        timmy.dot(20, random.choice(rgb_list))
        timmy.forward(50)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)



screen.exitonclick()


