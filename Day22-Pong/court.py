from turtle import Turtle

X_BOUND = 450
Y_BOUND = 250

class Court(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.color("blue")
        self.goto(-X_BOUND, -Y_BOUND)
        self.pendown()
        self.goto(-X_BOUND, Y_BOUND)
        self.goto(X_BOUND, Y_BOUND)
        self.goto(X_BOUND, -Y_BOUND)
        self.goto(-X_BOUND, -Y_BOUND)
        # Create Net
        self.goto(0, -Y_BOUND)
        self.color("Orange")
        self.setheading(90)
        for x in range(1, 2*Y_BOUND, 25):
            self.forward(25)
            if x % 2 == 1:
                self.penup()
            else:
                self.pendown()
