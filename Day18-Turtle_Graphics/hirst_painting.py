import colorgram
import turtle as t
from turtle import Screen, Turtle
from random import choice, randint

t.colormode(255)
tim = Turtle()
tim.penup()
tim.setposition(0, 0)
#extract color list
colors = colorgram.extract('hirstpainting.jpg', 20)
rgb_list = []

for item in colors:
    rgb_list.append(item.rgb)

def drawLine(gs):
    for x in range(gs-1):
        tim.dot(20, choice(rgb_list))
        tim.forward(30)

def moveRight():
    tim.right(90)
    tim.forward(30)
    tim.right(90)

def moveLeft():
    tim.left(90)
    tim.forward(30)
    tim.left(90)

grid_size = 10
for x in range(grid_size):
    drawLine(grid_size)
    if x % 2 == 0:
        moveLeft()
    else:
        moveRight()

screen = Screen()
screen.exitonclick()
