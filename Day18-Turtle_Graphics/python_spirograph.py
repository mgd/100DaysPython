import turtle as t
from turtle import Screen, Turtle
from random import randint, choice

t.colormode(255)
tim = Turtle()
tim.speed(0)

def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

for x in range(36):
    tim.color(rand_color())
    tim.circle(70)
    tim.right(10)

screen = Screen()
screen.exitonclick()
