from turtle import Turtle


class Score(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.goto(x, y)
        self.score = 0
        self.update()

    def increase(self):
        self.clear()
        self.score = +1
        self.update()

    def update(self):
        self.write(self.score, align="center", font=("Arial", 24, "normal"))
