import turtle as t
from random import choice, randint

t.colormode(255)
angles = [0, 90, 180, 270]
tim = t.Turtle()
tim.width(10)


def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

for x in range(100):
    tim.color(rand_color())
    tim.right(choice(angles))
    tim.forward(20)

screen = t.Screen()
screen.exitonclick()

