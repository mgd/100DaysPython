from turtle import Screen
from score import Score
from court import Court
from ball import Ball
from paddles import Paddles
import time
# CONSTANTS FOR SCORES POSITION
P1X = -50
P1Y = 250
P2X = 50
P2Y = 250

def up1():
    paddle1.up()

def down1():
    paddle1.down()

def up2():
    paddle2.up()

def down2():
    paddle2.down()




if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor("black")
    screen.listen()

    # Key Bindings
    screen.onkey(up2, "Up")
    screen.onkey(down2, "Down")
    screen.onkey(up1, "w")
    screen.onkey(down1, "s")

    # Court Settings
    court = Court()
    p1Score = Score(P1X, P1Y)
    p2Score = Score(P2X, P2Y)

    paddle1 = Paddles(1)
    paddle2 = Paddles(2)

    ball = Ball()
    game = True
    while game:
        screen.update()
        #Check if Ball hit top or botom wall
        x, y = ball.pos()
        if y >= 240:
            ball.top_bounce()
        elif y <= -240:
            ball.bottom_bounce()

        #Check if paddle is there to hit ball
        if 410 < x < 430:
            for p in paddle2.segs:
                if p.distance(ball) < 20:
                    ball.paddle_bounce()
                    p2Score.increase()

        elif -410 > x > -430:
            for p in paddle1.segs:
                if p.distance(ball) < 20:
                    ball.paddle_bounce()
                    p1Score.increase()
        ball.forward(5)
        if x >= 430 or x <= -430:

            game = False
    screen.exitonclick()