from turtle import Screen, Turtle
from random import randint

color_list = ["red", "green", "blue", "yellow", "purple"]

turtle_list = []
for x in range(0, 5):
    temp = Turtle()
    temp.color(color_list[x])
    temp.penup()
    temp.shape("turtle")
    temp.goto(x=-250, y=(-150 + 50 * x))
    turtle_list.append(temp)


for x in range(0, 500, 5):
    for turt in turtle_list:
        turt.forward(randint(1,5))

winner = (0.0, turtle_list[0])
for turt in turtle_list[1:]:
    x, y = turt.position()
    if winner[0] < x:
        winner = (x, turt)

print(f"The {(winner[1].color())[1]} turtle is the winner")
screen = Screen()
screen.exitonclick()