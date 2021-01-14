from turtle import Turtle, Screen
from random import choice
colors = ["red", "blue", "green", "yellow", "brown", "purple"]

tim = Turtle()
for x in range(3, 10):
    angle = 360 / x
    tim.pencolor(choice(colors))
    for y in range(x):
        tim.forward(50)
        tim.right(angle)

screen = Screen()
screen.exitonclick()