from turtle import Screen
from paddle import Paddle
from ball import Ball
from scores import Scores
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game 2022")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scores_a = Scores((-100, 275))
scores_b = Scores((100, 275))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 375:
        scores_a.get_point()
        ball.reset()
    if ball.xcor() < -375:
        scores_b.get_point()
        ball.reset()














screen.exitonclick()