from turtle import Screen
from snakeclass import Snake
import time

# Globals

snake = Snake()


def up():
    snake.up()


def down():
    snake.down()


def left():
    snake.left()


def right():
    snake.right()


if __name__ == "__main__":

    screen = Screen()
    screen.bgcolor("black")
    screen.tracer(0)
    screen.listen()

    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    alive = True

    while snake.alive():
        time.sleep(.1)
        snake.moveForward()
        screen.update()

    screen.exitonclick()
