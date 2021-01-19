from turtle import Turtle, Screen
from random import randint

direction = {'n': 90, 'up': 90, 's': 270, 'down': 270, 'e': 0, 'right': 0, 'w': 180, 'left': 180}

class Snake:

    def __init__(self):
        self.makeGrid()
        self.Snakes = []
        self.Snakes.append(self.newSnake(0, 0))
        self.newFood()

    def makeGrid(self):
        grid = Turtle()
        grid.speed('fastest')
        grid.color('blue')
        grid.hideturtle()
        grid.penup()
        grid.goto(-250, -250)
        grid.pendown()
        grid.goto(-250, 250)
        grid.goto(250, 250)
        grid.goto(250, -250)
        grid.goto(-250, -250)

    def newSnake(self, x, y):
        new = Turtle()
        new.penup()
        new.color("white")
        new.shape("circle")
        new.setposition(x, y)
        return new

    def moveForward(self):
        lastx, lasty = self.Snakes[-1].pos()
        # If only one exist, loop never starts
        for i in range(len(self.Snakes) - 1, 0, -1):
            x = self.Snakes[i-1].xcor()
            y = self.Snakes[i-1].ycor()
            self.Snakes[i].goto(x, y)
        self.Snakes[0].forward(10)

        if self.food.pos() == self.Snakes[0].pos():
            print("hit")
            self.refresh()
            self.Snakes.append(self.newSnake(lastx, lasty))

    def newFood(self):
        self.food = Turtle()
        self.food.penup()
        self.food.shape("square")
        self.food.color("blue")
        self.refresh()

    def refresh(self):
        pos = randint(-24, 24) * 10, randint(-24, 24) * 10
        self.food.goto(pos)

    def alive(self):
        head = self.Snakes[0]

        if head.xcor() == 250 or head.xcor() == -250:
            self.gameOver()
            return False
        elif head.ycor() == 250 or head.ycor() == -250:
            self.gameOver()
            return False

        for snake in self.Snakes[1:]:
            if snake.pos() == head:
                self.gameOver()
                return False

        return True

    def gameOver(self):
        over = Turtle()
        over.hideturtle()
        over.color("white")
        over.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def down(self):
        heading = self.Snakes[0].heading()
        if heading == direction['s'] or heading == direction['n']:
            pass
        elif heading == direction['e']:
            self.Snakes[0].right(90)
        elif heading == direction['w']:
            self.Snakes[0].left(90)

    def up(self):
        heading = self.Snakes[0].heading()
        if heading == direction['n'] or heading == direction['s']:
            pass
        elif heading == direction['e']:
            self.Snakes[0].left(90)
        elif heading == direction['w']:
            self.Snakes[0].right(90)

    def left(self):
        heading = self.Snakes[0].heading()
        if heading == direction['e'] or heading == direction['w']:
            pass
        elif heading == direction['n']:
            self.Snakes[0].left(90)
        elif heading == direction['s']:
            self.Snakes[0].right(90)

    def right(self):
        heading = self.Snakes[0].heading()
        if heading == direction['e'] or heading == direction['w']:
            pass
        elif heading == direction['n']:
            self.Snakes[0].right(90)
        elif heading == direction['s']:
            self.Snakes[0].left(90)
