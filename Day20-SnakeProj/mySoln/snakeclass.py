from turtle import Turtle, Screen
from random import randint

direction = {'n': 90, 'up': 90, 's': 270, 'down': 270, 'e': 0, 'right': 0, 'w': 180, 'left': 180}

class Snake:

    def __init__(self, currentHeading):
        s = Turtle()
        s.color("white")
        self.Snakes = []
        self.Snakes.append(self.newSnake(0, 0, direction['e']))
        self.food = self.newFood()


    def newSnake(self, x, y, angle):
        if angle == 0:
            angle = 360
        new = Turtle()
        new.penup()
        new.degrees(angle)
        new.color("white")
        new.shape("square")
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
            self.food = self.newFood()
            self.Snakes.append(self.newSnake(lastx, lasty, 0))

    def newFood(self):
        pos = randint(-25, 25) * 10, randint(-25, 25) * 10
        food = Turtle()
        food.penup()
        food.shape("square")
        food.color("white")
        food.goto(pos)
        return food

    def alive(self):
        head = self.Snakes[0]

        if head.xcor() == 250 or head.xcor() == -250:
            return False
        elif head.ycor() == 250 or head.ycor() == -250:
            return False

        for snake in self.Snakes[1:]:
            if snake.pos() == head:
                return False

        return True

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