from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.setheading(45)

    def paddle_bounce(self):
        self.setheading(270 + self.heading())

    def top_bounce(self):
        self.setheading(360 - self.heading())

    def bottom_bounce(self):
        self.setheading(360 - self.heading())
