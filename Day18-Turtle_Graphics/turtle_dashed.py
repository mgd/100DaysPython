from turtle import Turtle, Screen

tim = Turtle()

for x in range(20):
    if x % 2 == 0:
        tim.pendown()
    else:
        tim.penup()

    tim.forward(5)

screen = Screen()
screen.exitonclick()