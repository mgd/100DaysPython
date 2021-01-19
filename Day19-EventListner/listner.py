from turtle import Screen, Turtle

tim = Turtle()
screen = Screen()

def moveForward():
    tim.forward(10)

def moveBackwards():
    tim.backward(10)

def counterClock():
    tim.left(5)

def clockWise():
    tim.right(5)

def clear():
    tim.clear()
    tim.setposition(0,0)


#Bind a key stroke to event
screen.onkey(moveForward, "w")
screen.onkey(moveBackwards, "s")
screen.onkey(counterClock, "a")
screen.onkey(clockWise, "d")
screen.onkey(clear, "c")
screen.listen()
screen.exitonclick()
