from turtle import Turtle

X_LEFT = -430
X_RIGHT = 430
PADDLE_TOP = 30
PADDLE_BOTTOM = -30
class Paddles:

    def __init__(self, player):
        self.segs = []
        if player == 1:
            x_cord = X_LEFT
        else:
            x_cord = X_RIGHT

        for y in range(PADDLE_BOTTOM, PADDLE_TOP, 10):
            turt = Turtle()
            turt.penup()
            turt.speed("fastest")
            turt.color("white")
            turt.shape("square")
            turt.goto(x_cord, y)
            self.segs.append(turt)


    def up(self):
        for turt in self.segs:
            turt.setheading(90)
            turt.forward(10)

    def down(self):
        for turt in self.segs:
            turt.setheading(270)
            turt.forward(10)

